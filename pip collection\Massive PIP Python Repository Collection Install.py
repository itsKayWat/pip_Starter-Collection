import subprocess
import sys

# List of commonly used packages
packages = [
    # Data Science & Machine Learning
    "numpy", "pandas", "scipy", "scikit-learn", "matplotlib", "seaborn",
    "tensorflow", "torch", "keras", "xgboost", "lightgbm",
    
    # Web Development
    "flask", "django", "fastapi", "requests", "beautifulsoup4",
    "selenium", "aiohttp",
    
    # Database
    "sqlalchemy", "pymongo", "psycopg2-binary", "mysql-connector-python",
    
    # Utility & Tools
    "pytest", "black", "pylint", "mypy", "poetry",
    "python-dotenv", "pyyaml", "tqdm", "pillow",
    
    # API & JSON
    "fastapi", "pydantic", "uvicorn", "jsonschema",
    
    # Documentation
    "sphinx", "mkdocs",
]

def install_packages():
    print("Starting package installation...")
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")
        except Exception as e:
            print(f"Error installing {package}: {str(e)}")
    
    print("\nInstallation process completed!")

if __name__ == "__main__":
    install_packages()