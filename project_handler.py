import os
import shutil
from colorama import init , Fore, Style
import machine_select
 
init() # colorama initialization

PROJECT_FOLDER_PATH, WEB_DEV_FOLDER_PATH = machine_select.select_machine()


# creates python projects
def create_project(name):

    os.mkdir(name)  # Creates the directory with the specified name
    os.chdir(os.path.join(PROJECT_FOLDER_PATH, name))  # Changes to new directory
    # Creates main.py with new project-specific content
    with open('main.py', 'w') as file:
        file.write(f"# Project Name: {name}\n\nprint(\"Hello World!\")")

    print(Fore.GREEN + "\nProject created!" + Style.RESET_ALL)
    os.startfile(PROJECT_FOLDER_PATH)  # Opens project folder path displaying new project creation
    os.chdir(os.path.join(PROJECT_FOLDER_PATH)) # change directory back to project path for new creation
    return

# creates webdev projects
def create_webdevkit(name):
    boiler_plate_text = f"{PROJECT_FOLDER_PATH}\\prac_script_01\\boilerplate.txt"
    global_css_text = f"{PROJECT_FOLDER_PATH}\\prac_script_01\\globalcss.txt"
    destination_file_path = os.path.join(WEB_DEV_FOLDER_PATH, name)
     
    try:
        os.mkdir(name)
        os.chdir(destination_file_path)

        # create assets folder
        os.mkdir("assets")
        os.chdir("assets")
        os.mkdir("img")
        os.chdir("..")

        # create styles folder 
        os.mkdir("css")
        os.chdir("css") # changes directory to newly made css folder
        with open("styles.css", "w") as file:
            file.write(f"/* Project {name} styles file */")
        
        with open(global_css_text, "r") as global_css_file:
            global_css_content = global_css_file.read()
        
        with open("global.css", "w") as file:
            file.write(global_css_content)
        os.chdir("..")

        # create javascript folder
        os.mkdir("js")
        os.chdir("js")
        with open("index.js", "w") as file:
            file.write(f"// Project {name} js file")

        #create index.html file
        os.chdir("..")
        # read content from the srouce file
        with open(boiler_plate_text, "r") as boiler_plate_file:
            content = boiler_plate_file.read()

        with open("index.html", "w") as file:
            file.write(content)

        print(Fore.GREEN + "\nWeb development project initialized!" + Style.RESET_ALL)
        os.startfile(WEB_DEV_FOLDER_PATH)
        os.chdir(WEB_DEV_FOLDER_PATH)
        
    except Exception as e:
        print(f"\nERROR: {e}")

def delete_project(name):

    dir_path = f"{PROJECT_FOLDER_PATH}\\{name}"
    dir_path_webdev = f"{WEB_DEV_FOLDER_PATH}\\{name}"

    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        print(Fore.GREEN + f"{dir_path}\nValid path...\nRemoving {name}" + Style.RESET_ALL)
    elif os.path.exists(dir_path_webdev):
        shutil.rmtree(dir_path_webdev)
        print(Fore.GREEN + f"{dir_path}\nValid path...\nRemoving {name}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"{name} is not a valid project name." + Style.RESET_ALL)
    return

