import sys
import os
import time
import cv2

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from package_name import PickAndPlace

def main():
    pick_and_place = PickAndPlace()

    try:
        while True:
            if not pick_and_place.run():
                print("Stopping the process as no target was found.")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("Bin picking process interrupted.")
    finally:
        pick_and_place.camera.release()
        pick_and_place.xarm_disconnect()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()