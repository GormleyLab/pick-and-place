import time
from xarm.wrapper import XArmAPI
from roboflow import Roboflow
import cv2
import numpy as np
from .camera import RealSenseCamera


class PickAndPlace:
    def __init__(self):
        self.image_path = "captured_images/captured_image.jpg"
        self.camera = RealSenseCamera()
        self.rf = Roboflow(api_key="kaFbI9ITQ6PebFQE1FNK")

        self.xarm = XArmAPI("192.168.1.210")

        self.xarm.motion_enable(True)
        self.xarm.set_mode(0)
        self.xarm.set_state(0)
        self.xarm.set_gripper_mode(0)
        self.xarm.set_gripper_enable(True)
        self.xarm.set_gripper_speed(1000)

        self.home_position = [-159.3, -193.5, 329.4, 180, 0, -90]
        self.place_position = [-82.8, -418.1, 329.4, -180, 0, -120.5]
        self.safe_position = [357.2, 38.4, 225.3, -180, 0, 16.4]

        self.xarm.set_gripper_position(850, wait=True)
        self.xarm.set_position(*self.home_position[:6], speed=400, wait=True)

        self.tolerance = 10
        self.move_increment = 10

        self.project = self.rf.workspace().project("detect-boxes-yzqdp")
        self.model = self.project.version(2).model

    def move(self, location):
        print("Moving to", location)
        self.xarm.set_position(*location[:6], speed=400, wait=True)

    def xarm_disconnect(self):
        self.xarm.disconnect()

    def capture_image(self):
        print("Capturing image")
        image = self.camera.get_frame()
        if image is None:
            print("Failed to capture image")
        cv2.imwrite(self.image_path, image)
        return image

    def detect_objects(self):
        print("Detecting objects")
        result = self.model.predict(self.image_path, confidence=50, overlap=30)
        print("Predictions made")
        result.save("prediction.jpg")
        print("Image saved")

        result_json = result.json()
        print("converted to json")
        print(result_json)

        prediction = result_json["predictions"]

        return prediction

    def select_most_centered_object(self, objects):
        print("Selecting most centered object")
        if not objects:
            return None

        image_center = (320, 240)
        objects.sort(
            key=lambda obj: (obj["x"] - image_center[0]) ** 2
            + (obj["y"] - image_center[1]) ** 2
        )
        return objects[0]

    def center_object_in_frame(self, target, image):
        image_center_x = 320
        image_center_y = 240
        calibration_factor = 0.8
        
        angle = self.find_rotation(target, image)

        while target is not None:
            img_x = target["x"]
            img_y = target["y"]
            x_offset = img_x - image_center_x
            y_offset = img_y - image_center_y
            
            xarm_angle = (self.xarm.position[5] + 90)*-1

            x_robot = (x_offset * np.cos(np.radians(xarm_angle)) - y_offset * np.sin(
                np.radians(xarm_angle))) * calibration_factor + self.xarm.position[0]
            y_robot = self.xarm.position[1] - (x_offset * np.sin(np.radians(xarm_angle)) + y_offset * np.cos(
                np.radians(xarm_angle))) * calibration_factor

            print(
                f"Current xarm position: ({self.xarm.position[0]}, {self.xarm.position[1]})"
            )

            print(
                f"Current object position: ({img_x}, {img_y}), offsets: ({x_offset}, {y_offset})"
            )
            
            print(
                f"GOTO Xarm position: ({x_robot}, {y_robot})"
            )

            if abs(x_offset) <= self.tolerance and abs(y_offset) <= self.tolerance:
                print("Object is centered")
                break

            self.move(
                [
                    x_robot,
                    y_robot,
                    self.xarm.position[2],
                    180,
                    0,
                    angle,
                ]
            )

            time.sleep(1)
            image = self.capture_image()
            objects = self.detect_objects()
            target = self.select_most_centered_object(objects)

            if target is None:
                print("Failed to re-detect the object after centering attempt")
                break

    def find_rotation(self, target, image):
        x_max = int(target["x"] + target["width"] / 2)
        x_min = int(target["x"] - target["width"] / 2)
        y_max = int(target["y"] + target["height"] / 2)
        y_min = int(target["y"] - target["height"] / 2)

        cropped = image[y_min:y_max, x_min:x_max]
        gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 50, 150)

        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)

            rect = cv2.minAreaRect(largest_contour)
            box = cv2.boxPoints(rect)
            box = np.int32(box)
            rect_angle = rect[2]
            x = int(rect[0][0]) - 50
            y = int(rect[0][1])

            cv2.drawContours(cropped, [box], 0, (0, 255, 0), 2)
            cv2.putText(
                cropped,
                f"Angle: {rect_angle:.2f} degrees",
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                2,
            )
        return rect_angle * -1

    def convert_coordinates(self, target):
        image_center_x = 363
        image_center_y = 163
        calibration_factor = 0.8

        img_x = target["x"]
        img_y = target["y"]
        x_offset = img_x - image_center_x
        y_offset = img_y - image_center_y

        xarm_angle = (self.xarm.position[5] + 90)*-1

        x_robot = (x_offset * np.cos(np.radians(xarm_angle)) - y_offset * np.sin(
            np.radians(xarm_angle))) * calibration_factor + self.xarm.position[0]
        y_robot = self.xarm.position[1] - (x_offset * np.sin(np.radians(xarm_angle)) + y_offset * np.cos(
            np.radians(xarm_angle))) * calibration_factor

        print(
            f"Image coordinates: ({img_x}, {img_y}) -> Robot coordinates: ({x_robot}, {y_robot})"
        )

        return x_robot, y_robot

    def run(self):
        image = self.capture_image()
        self.camera.show_image(image)

        if image is not None:
            objects = self.detect_objects()
            target = self.select_most_centered_object(objects)
            print(target)

            if target:
                self.center_object_in_frame(target, image)

                image = self.capture_image()
                objects = self.detect_objects()
                target = self.select_most_centered_object(objects)

                if target:
                    x_robot, y_robot = self.convert_coordinates(target)

                    if (
                        x_robot > 150
                        or x_robot < -300
                        or y_robot > -100
                        or y_robot < -400
                    ):
                        print("Invalid coordinate: Skipping this target.")
                        return

                    print(f"Moving to pick position: {x_robot}, {y_robot}, 50")
                    self.move(
                        [x_robot, y_robot, 50, -180, 0, self.xarm.position[5]]
                    )
                    print(f"Moving down to pick: {x_robot}, {y_robot}, 0")
                    self.move(
                        [x_robot, y_robot, 0, -180, 0, self.xarm.position[5]]
                    )
                    self.xarm.set_gripper_position(270, wait=True)
                    print("Moving to place position")
                    self.move(self.place_position)
                    self.xarm.set_gripper_position(850, wait=True)
                    self.move(self.home_position)
                    return True
                else:
                    print("No target found after centering")
                    return False
            else:
                print("No target found")
                return False
        else:
            print("No image captured")
            return False