import os
import argparse
import subprocess

# Function to create the basic FastAPI project structure
def create_fastapi_project(project_name):
    # Project structure
    directories = [
        f"{project_name}",
        f"{project_name}/app",
    ]
    files = {
        f"{project_name}/app/main.py": '''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
''',
        f"{project_name}/app/__init__.py": "",
        f"{project_name}/requirements.txt": "fastapi\nuvicorn\n",
        f"{project_name}/.gitignore": "venv\n__pycache__/\n.env\n",
    }

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create files with content
    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content)

    print(f"FastAPI project '{project_name}' created successfully!")


# Function to run FastAPI development server
def run_fastapi_server():
    subprocess.run(["uvicorn", "app.main:app", "--reload"])


# Setup the argument parser
def main():
    parser = argparse.ArgumentParser(description="FastAPI Admin: A command-line tool for FastAPI projects")
    parser.add_argument("command", choices=["startproject", "runserver"], help="The command to run (e.g., 'startproject', 'runserver')")
    parser.add_argument("project_name", nargs="?", help="The name of the project to create (required for 'startproject')")

    args = parser.parse_args()

    if args.command == "startproject" and args.project_name:
        create_fastapi_project(args.project_name)
    elif args.command == "runserver":
        run_fastapi_server()
    else:
        print("Error: 'startproject' requires a project name.")
