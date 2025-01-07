"""
simple distributed control version system
"""
import os
import shutil
import datetime
import json

STATUS = True

def init():
    "initialize repository"
    os.mkdir(".repository")

    with open(".repository/versions.json", "w", encoding="UTF-8") as db_json:
        db_json.write("[]")

def save(file, version, message):
    "save changes"
    try:
        with open(file, "r", encoding="UTF-8") as content:
            content = content.read()

        if os.path.exists(f".repository/{file}"):
            os.remove(f".repository/{file}")
            shutil.copy(file, ".repository")

            data = {
                "version": version,
                "message": message,
                "timestamp" : datetime.datetime.now().isoformat(),
                "content":  content
            }

            with open(".repository/versions.json", "r", encoding="UTF-8") as jsonfile:
                get_data = jsonfile.read()

            get_data = json.loads(get_data)
            for el in get_data:
                if el["file"] == file:
                    el["versions"].append(data)

            json_modified = json.dumps(get_data)
            with open(".repository/versions.json", "w", encoding="UTF-8") as jsonfile:
                jsonfile.write(json_modified)

        else:
            shutil.copy(file, ".repository")
            data = {
                "file": file,
                "versions" : [
                    {
                        "version": version,
                        "message": message,
                        "timestamp" : datetime.datetime.now().isoformat(),
                        "content":  content
                    }
                ]
            }

            with open(".repository/versions.json", "r", encoding="UTF-8") as jsonfile:
                get_data = jsonfile.read()

            get_data = json.loads(get_data)
            get_data.append(data)

            json_modified = json.dumps(get_data)
            with open(".repository/versions.json", "w", encoding="UTF-8") as jsonfile:
                jsonfile.write(json_modified)

    except ValueError:
        print("Invalid option, try again")

def restore(file, version):
    "restore version"
    try:
        with open(".repository/versions.json", "r", encoding="UTF-8") as jsondata:
            get_restore_data = jsondata.read()

            get_restore_data = json.loads(get_restore_data)

        for item in get_restore_data:
            for key_item in item["versions"]:
                if key_item["version"] == version:
                    restore_code = key_item["content"]
                    with open(f".repository/{file}", "w", encoding="UTF-8") as restore_file:
                        restore_file.write(restore_code)

    except ValueError:
        print("Invalid option, try again")

def cambiar_directorio(route):
    """change directory"""
    try:
        os.chdir(route)
        print(os.getcwd())
    except FileNotFoundError:
        print(f"Error: directory not found '{route}'.")

while STATUS is True:
    user_command = input("$ ").lower()
    if user_command == "init":
        init()

    elif user_command == "save":
        file_to_add, add_version, save_message = input("$...").split(maxsplit=2)
        save(file_to_add, str(add_version), save_message)

    elif user_command == "list":
        try:    
            with open(".repository/versions.json", "r", encoding="UTF-8") as recordfile:
                record = json.load(recordfile)
                for element in record:
                    print("\nfile: ", element["file"])
                    for key in element["versions"]:
                        print("version: ", key["version"], " message: ",
                            key["message"], " timestamp: ", key["timestamp"])

        except ValueError:
            print("you shouldn't see this")

    elif user_command == "restore":
        file_to_restore, version_to_restore = input("$...").split(maxsplit=1)
        restore(file_to_restore, str(version_to_restore))

    elif user_command == "help":
        print("INIT: create the repository")
        print("SAVE: commit file, arguments: file, version (1.0), message")
        print("LIST: change history")
        print("RESTORE: restore version, arguments: file, version to restore")
        print("CD: change directory")
        print("LS: list directories")
        print("PWD: print working directory")
        print("EXIT: bye :)")

    elif user_command.startswith("cd "):
        ruta = user_command[3:].strip()
        cambiar_directorio(ruta)

    elif user_command == "cd ..":
        cambiar_directorio("..")

    elif user_command == "ls":
        for items in os.listdir():
            print(items)

    elif user_command == "pwd":
        print(os.getcwd())

    elif user_command == "exit":
        STATUS = False

    elif user_command == "cls":
        os.system("cls")

    else:
        print('try "help"')
