# 0x00 AirBnB clone | The Console

<p align="center">
<img src="https://i.imgur.com/JOhaZ5m.png">
</p>


# AirBnB Clone - Console

This directory contains an implementation of an AirBnB clone. The initial focus is on the development of the console, which enables the creation, updating, deletion, and management of different classes and attributes for items and users within the application.

## The Console

The console provides the following functionalities:

- Creation of a data model
- Management (create, update, destroy, etc.) of objects via a console/command interpreter
- Storage and persistence of objects to a file (JSON file)

The first step involves the manipulation of a powerful storage system. This storage engine acts as an abstraction between "My object" and "How they are stored and persisted." It allows seamless handling of storage concerns without affecting the command interpreter and front-end or RestAPI components. This abstraction also facilitates easy changes to the type of storage without requiring updates to the entire codebase. The console serves as a tool to validate this storage engine.

## Command Interpreter

The command interpreter resembles a mini-shell, enabling the management of project objects. It supports the following operations:

- Creating a new object (e.g., a new User or a new Place)
- Retrieving an object from a file, database, etc.
- Performing operations on objects (count, compute stats, etc.)
- Updating attributes of an object
- Destroying an object

## Project Objectives

The project focuses on achieving the following objectives:

- Creating a Python package
- Developing a command interpreter in Python using the cmd module
- Implementing Unit testing in a large project
- Serializing and deserializing a Class
- Reading and writing a JSON file
- Managing datetime
- Understanding UUIDs
- Exploring *args and **kwargs and their usage
- Handling named arguments in a function

## Directory Contents

- **Models Folder:** Contains classes of the project. `BaseModel` serves as the parent class, and other classes (amenity, city, place, review, state, user) inherit from `BaseModel` while specifying additional attributes.
- **Tests Folder:** Includes unit tests for the project.
- **AUTHORS:** Information about the authors.
- **console.py:** Executable file for the console.
- **file.json:** JSON file containing information about instances.

---

## Table of Contents

- [Examples and Usage](#examples-and-usage)
- [Installation](#installation)
- [Documentation](#documentation)
- [Contributing](#contributing)
-
-----------

# Examples of Usage

### Execution ###
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
-----------
## Installation

* Clone the repository. git clone https://github.com/MMMBenchahyd/AirBnB_clone.git
* Open the /AirBnB_clone directory and execute console.py

### Setup

* You need Python interpreter.
IMPORTANT: The project was created in Ubuntu 20.04 LTS using python3 (version 3.8.5)

-----------
## Authors

* **BENCHAHYD** - [github](https://github.com/MMMBenchahyd) - [linkedin](https://www.linkedin.com/in/mhammed-benchahyd-aa1198281/) - [X](https://twitter.com/SEMhammedBen)
* **Zakariia** - [github]()
