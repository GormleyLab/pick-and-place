# GL-template
**Gormley Lab Python Project Template**

A beginner-friendly Python project template that follows best practices and provides a solid foundation for new projects in the Gormley Lab.

## 🚀 Quick Start

1. **Use this template** to create a new repository
2. **Rename the package**: Change `src/package_name/` to `src/your_project_name/`
3. **Update metadata**: Edit `src/your_project_name/__about__.py` with your project details
4. **Install dependencies**: `pip install -r requirements.txt`
5. **Run the example**: `python main.py`

## 📁 Project Structure

This template follows the **src layout**, a Python best practice that keeps your source code organized and separate from tests, documentation, and configuration files.

```
GL-template/
├── main.py                          # 🎯 Entry point - run this file to start your program
├── requirements.txt                 # 📦 List of Python packages your project needs
├── README.md                       # 📖 Project documentation (this file)
├── LICENSE                         # ⚖️ Legal terms for using your code
├── attachment/                     # 📎 Store additional files and resources
├── data/                           # 📊 Store datasets, CSV files, and raw data
├── docs/                           # 📚 Documentation files and project notes
├── imgs/                           # 🖼️ Images, plots, and visual outputs
├── jsons/                          # 📋 JSON configuration and data files
├── models/                         # 🤖 Machine learning models and saved weights
├── notebook/                       # 📓 Jupyter notebooks for analysis and experimentation
└── src/                            # 📂 Source code directory
    └── package_name/               # 🐍 Your Python package (rename this!)
        ├── __init__.py             # 🔧 Makes this directory a Python package
        ├── __about__.py            # ℹ️ Package metadata (version, author, etc.)
        ├── class_example.py        # 🏗️ Example class demonstrating OOP concepts
        └── utils_example.py        # 🛠️ Utility functions for common tasks
```

## 📚 Understanding the Components

### Entry Point (`main.py`)
- **Purpose**: The file you run to start your program
- **What it does**: Imports your package and demonstrates its usage
- **Key concept**: Uses `if __name__ == "__main__"` to ensure code only runs when executed directly

### Package Directory (`src/package_name/`)
- **Rename this** to match your project (use lowercase with underscores: `my_awesome_project`)
- Contains all your project's source code
- The `__init__.py` file makes it importable as a package

### Core Files Explained

| File | Purpose | When to modify |
|------|---------|----------------|
| `__init__.py` | Controls what gets imported from your package | When adding new classes/functions |
| `__about__.py` | Stores project metadata (version, author, description) | At project start and version updates |
| `class_example.py` | Template for object-oriented code | Replace with your own classes |
| `utils_example.py` | Template for utility functions | Add general-purpose functions here |

## 🎯 Getting Started Guide

### Step 1: Customize Your Package
```bash
# Rename the package directory
mv src/package_name src/my_project_name

# Update imports in main.py to match your new package name
# Change: from package_name import ...
# To:     from my_project_name import ...
```

### Step 2: Update Package Metadata
Edit `src/my_project_name/__about__.py`:
```python
__title__ = "My Awesome Project"
__description__ = "What your project does"
__version__ = "1.0.0"
__author__ = "Your Name"
__author_email__ = "your.email@example.com"
```

### Step 3: Add Your Code
- **Classes**: Add new `.py` files for your classes in the package directory
- **Functions**: Use `utils_example.py` or create new utility files
- **Imports**: Update `__init__.py` to export your new classes and functions

### Step 4: Manage Dependencies
Add any Python packages you need to `requirements.txt`:
```
numpy
pandas
matplotlib
```

## 🏗️ Development Best Practices

### Object-Oriented Programming (OOP)
- **Use classes** for complex data structures and behaviors
- **Follow naming conventions**: `ClassName` (PascalCase) for classes, `function_name` (snake_case) for functions
- **Document your code** with docstrings

### Project Organization
- **Keep related code together** in the same file or subdirectory
- **Use descriptive names** for files, classes, and functions
- **Separate concerns**: classes for objects, utils for general functions

### Version Control
- **Commit early and often** with descriptive messages
- **Use .gitignore** to exclude temporary files
- **Tag releases** when you reach milestones

## 🔧 Common Tasks

### Adding a New Class
1. Create a new `.py` file in your package directory
2. Define your class with proper docstrings
3. Import it in `__init__.py`
4. Add it to the `__all__` list

### Adding Dependencies
1. Add the package name to `requirements.txt`
2. Install with `pip install -r requirements.txt`
3. Import and use in your code

### Testing Your Code
```bash
# Run your program
python main.py

# Check for syntax errors
python -m py_compile src/your_package_name/*.py
```

## 📖 Learning Resources

- **Python Classes**: [Official Python Tutorial on Classes](https://docs.python.org/3/tutorial/classes.html)
- **Package Structure**: [Python Packaging Guide](https://packaging.python.org/)
- **Best Practices**: [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)

## 🤝 Contributing

This template is designed for the Gormley Lab. Feel free to suggest improvements or report issues to help other lab members get started with Python development.

---

**Happy coding!** 🐍✨