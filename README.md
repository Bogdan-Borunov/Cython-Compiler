# Cython-Compiler

An interactive command-line tool for creating, compiling, and managing Cython modules with English and Russian language support.

Cython-Compiler simplifies common Cython development tasks by providing an interactive terminal menu and a convenient command-based workflow.

## Motivation

Working with Cython files often involves repetitive tasks such as creating source files, compiling modules, and preparing Python files to import compiled code.

Cython-Compiler was created to make these tasks easier through a simple command-line interface. The project also provides bilingual support, making it more accessible to both English-speaking and Russian-speaking developers.

## Quick Start

### Prerequisites

Before using Cython-Compiler, make sure you have:

- Python installed.
- A compatible C compiler configured on your system.
- Git installed to clone the repository.

### 1. Clone the repository

```bash
git clone https://github.com/Bogdan-Borunov/Cython-Compiler.git
cd Cython-Compiler
```

### 2. Install dependencies

Install the required Python packages:

```bash
python -m pip install cython setuptools art
```

### 3. Run the application

Start the interactive compiler:

```bash
python compiler.py
```

The application opens an interactive terminal menu in the selected language.

## Usage

Cython-Compiler provides commands for managing Cython source files directly from the terminal.

### Available commands

| Command | Description |
|---|---|
| `/help` | Display the available commands. |
| `/start FILE.pyx` | Compile an existing Cython source file. |
| `/create FILE.pyx` | Create and compile a new Cython source file. |
| `/import MODULE_NAME` | Generate a Python file that imports a Cython module. |
| `/settings` | Open application settings. |
| `/lan` | Change the interface language. |
| `/github` | Display the project's GitHub repository link. |
| `/exit` | Exit the application. |

Replace `FILE.pyx` or `MODULE_NAME` with the appropriate filename or module name when using a command.

### Example workflow

1. Clone the repository and install the dependencies.
2. Start the application with `python compiler.py`.
3. Enter `/help` to view the available commands.
4. Use `/create example.pyx` to create and compile a Cython source file.
5. Use `/start example.pyx` to compile an existing source file.
6. Use `/lan` to change the interface language when needed.

### Language support

The application supports English and Russian.

Use the `/lan` command and follow the interactive prompt to select your preferred language.

### Dependencies

The project uses the following Python packages:

- [Cython](https://cython.readthedocs.io/) — translates Cython source code into C or C++.
- [setuptools](https://setuptools.pypa.io/) — provides Python build and packaging tools.
- [art](https://pypi.org/project/art/) — provides text-art functionality.

A compatible C compiler may also be required to build compiled Cython modules.

## Contributing

Contributions, bug reports, and suggestions are welcome.

To contribute:

1. Fork the repository on GitHub.
2. Clone your fork to your local machine.
3. Create a branch for your changes.
4. Make your changes and test them locally.
5. Commit and push your changes to your fork.
6. Open a pull request describing your improvements.

Please keep contributions focused, document important changes, and verify that existing functionality continues to work.

## Project Structure

The main project files include:

- `compiler.py` — application entry point.
- `CompilerFunction.py` — compiler-related functionality.
- `languges.py` — language support.
- `setup.py` — project setup and packaging configuration.
- `CHANGELOG.md` — project change history.

## License

Please refer to the repository for licensing information.

## Author

Developed by [Bogdan Borunov](https://github.com/Bogdan-Borunov).

Project repository: [Cython-Compiler](https://github.com/Bogdan-Borunov/Cython-Compiler)