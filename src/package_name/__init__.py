# This is the __init__.py file for your package
# The __init__.py file tells Python that this directory is a Python package
# It controls what gets imported when someone does "from package_name import ..."

# Import version information from our metadata file
# The dot (.) before __about__ means "import from the same directory"
# This is called a relative import
from .__about__ import __version__

# Import our custom class from the class_example.py file
# Again, the dot means "from the same directory"
from .class_example import Class_name

# Import our utility function from the utils_example.py file
from .utils_example import function_name

# __all__ is a special variable that defines what gets exported from this package
# When someone does "from package_name import *", only these items will be imported
# This is a good practice to control your package's public interface
__all__ = ['Class_name', 'function_name', '__version__']