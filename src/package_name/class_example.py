# This file contains an example class definition
# Classes are a fundamental concept in object-oriented programming (OOP)
# They allow you to bundle data (attributes) and functionality (methods) together

class Class_name:  # Class names should follow PascalCase convention (first letter of each word capitalized)
    """
    This is an example class that demonstrates basic OOP concepts.
    
    A class is like a blueprint for creating objects. Each object created from this class
    will have the same structure but can hold different data.
    
    Attributes:
        message (str): A string message that the class will store and display
    """

    def __init__(self, message_input):
        """
        This is the constructor method - it's called when you create a new object from this class.
        
        The __init__ method is special in Python - it initializes new instances of the class.
        'self' refers to the specific instance being created.
        
        Args:
            message_input (str): The message to store in this instance
        """
        # self.message creates an instance variable (attribute)
        # This stores the message_input value so this specific object can remember it
        self.message = message_input
        
    def method_name(self):
        """
        This is an instance method - a function that belongs to this class.
        
        Instance methods can access and modify the object's attributes through 'self'.
        The 'self' parameter is automatically passed when you call the method on an object.
        
        This method prints the message stored in this instance.
        """
        # Access the instance variable we set in __init__
        print(self.message)