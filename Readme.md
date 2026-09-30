# KazeOS

> **KazeOS is a learning project built in Python to understand how operating-system concepts and command-line interfaces work.**

KazeOS is **not a real operating system**. It is a Python-based terminal simulation that I am building while learning programming, filesystem operations, error handling, and how command-line systems work.

The goal is to learn by building features step by step rather than trying to create a full operating system immediately.

## How KazeOS Works

KazeOS runs as a Python program and provides a simple command-line interface.

The basic flow is:

```text
User
  ↓
KazeOS Terminal
  ↓
Command Parser
  ↓
Command Function
  ↓
Python / OS Module
  ↓
Result
```

For example:

```text
KazeOS@admin: ls
```

The terminal receives the command, identifies `ls`, and calls the corresponding Python function.

That function can then use Python's `os` module to interact with the actual filesystem.

## Current Features

### Authentication

KazeOS currently has a simple username and password login system.

```text
username: admin
password: admin
logged in...
```

### Terminal Commands

Currently supported commands include:

* `help`
* `exit`
* `clear`
* `pwd`
* `ls`
* `cd`
* `mkdir`
* `calc`
* `rm`

### Filesystem Operations

KazeOS currently uses Python's `os` module for filesystem operations.

Examples:

```text
ls
ls terminal
cd terminal
cd ..
mkdir test
pwd
```

`cd` changes the program's current working directory using `os.chdir()`.

`ls` lists directory contents using `os.listdir()`.

`mkdir` creates directories using `os.makedirs()`.

### Error Handling

KazeOS also uses Python's exception handling system to deal with invalid commands and filesystem errors.

For example:

```text
KazeOS@admin: cd randomfolder
Location doesn't exist...
```

Instead of crashing the entire program, KazeOS catches the error and displays a message.

## Calculator

KazeOS includes a simple calculator that currently supports:

```text
calc 2 + 3
calc 5 - 2
calc 4 * 2
calc 10 / 2
```

The calculator is being developed separately and will become more capable over time.

## Project Structure

The project is currently organized into separate Python files so that different parts of KazeOS can be developed independently.

```text
KazeOS/
├── terminal/
│   ├── main.py
│   ├── qonsol.py
│   ├── commands.py
│   ├── calc.py
│   ├── config.py
│   └── os_detection.py
│
├── run.bat
└── README.md
```

The project structure may change as KazeOS grows.

## Why I'm Building This

KazeOS is mainly a way to learn Python through a real project.

While building it, I am learning about:

* Python modules and imports
* Functions
* Loops and conditions
* Exception handling
* Command parsing
* Filesystem operations
* Working directories
* Project structure
* How command-line interfaces work

The project is intentionally being built **one feature at a time**.

## Future Plans

Possible future features include:

* File creation and reading
* File deletion
* Better command parsing
* More robust error handling
* User permissions
* A simulated process system
* A simulated memory system
* More advanced shell features
* Eventually exploring how real operating systems work at a lower level

These features may change as I continue learning.

## Important

KazeOS is **not an operating system kernel** and does not replace Windows or Linux.

It is a Python learning project that **simulates some ideas found in operating systems and command-line environments**.

The main purpose of KazeOS is simple:

> **Learn by building.**
