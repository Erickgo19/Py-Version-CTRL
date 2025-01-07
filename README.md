# Simple Distributed Version Control System

This is a simple distributed version control system implemented in Python. It allows you to initialize a repository, save file versions, list the change history, and restore previous versions.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.

## Usage

### Available Commands

- `init`: Creates the repository.
- `save <file> <version> <message>`: Saves a version of the specified file with a message.
- `list`: Displays the change history.
- `list`: Displays the change history.
- `restore <file> <version>`: Restores a specific version of the file.
- `cd <path>`: Changes the current directory.
- `ls`: Lists the files and directories in the current directory.
- `pwd`: Displays the current working directory.
- `exit`: Exits the program.
- `cls`: Clears the screen.

### Usage Examples

#### Initialize the Repository

```sh
$ init

### Save a Version of a File

$ save
$... file.txt 1.0 "Version 1.0 message"

### List the Change History

$ list

### Restore a Version of a File

$ restore file.txt 1.0

### Change Directory

$ cd path/to/directory

### List Files and Directories

$ ls

### Display the Current Working Directory

$ pwd

### Exit the Program

$ exit

### Clear the Screen

$ cls

### Contributions
- Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

### License
- This project is licensed under the MIT License. See the LICENSE file for more details.
