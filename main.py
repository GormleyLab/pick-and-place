# This is the main entry point for your Python program
# When someone runs "python main.py", this file will be executed

# Import required modules
import sys  # sys module provides access to system-specific parameters and functions
import os   # os module provides operating system interface functions

# Add the 'src' directory to Python's path so we can import our custom package
# This allows Python to find modules in the src/ directory
# os.path.dirname(__file__) gets the directory where this main.py file is located
# os.path.join() safely combines path components regardless of operating system
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import our custom components from the package
# These imports come from src/package_name/__init__.py
from package_name import Class_name, function_name, __version__

def main():
    """
    Main function that demonstrates how to use the package components.
    This is where your program's logic should go.
    """
    # Print the version of our package (defined in __about__.py)
    print(f"Package version: {__version__}")
    
    # Create an instance (object) of our custom class
    # We pass "Hello, world!" as an argument to the class constructor
    object_name = Class_name("Hello, world!")
    
    # Call a method on our class instance
    # This will execute the method_name() function defined in the class
    object_name.method_name()
    
    # Call a standalone utility function
    # This function is defined in utils_example.py
    function_name()

# This is a Python idiom that ensures main() only runs when this file is executed directly
# If this file is imported as a module, main() won't run automatically
# __name__ is a special variable that Python sets to "__main__" when running the file directly
if __name__ == "__main__":
    main()