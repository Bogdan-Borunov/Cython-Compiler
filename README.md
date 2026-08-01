# 🚀 Cython Compiler

![Demo GIF](https://text-image.ru/_nw/65/63211419.gif)

## 🇺🇸 English Version

**Interactive compiler for Cython projects with English and Russian support.**
Create, compile, and manage `.pyx` modules directly from the terminal with a clear command system and a simple workflow.

---

## ✨ Features

* Interactive terminal menu
* Compile existing `.pyx` files
* Create new `.pyx` files automatically
* Generate `.py` import files for `.pyx` modules
* English / Russian interface
* Easy language switching with `/lan`
* Terminal-friendly workflow
* Active development and ongoing improvements

---

## 📂 Project Structure

```text
compiler.py
├── setup.py
├── CompilerFunction.py
└── languges.py
```

| File                  | Description                   |
| --------------------- | ----------------------------- |
| `compiler.py`         | Starts the compiler           |
| `setup.py`            | Interactive command interface |
| `CompilerFunction.py` | Core compilation logic        |
| `languges.py`         | Language strings              |

---

## 🚀 Getting Started

Run the compiler:

```bash
python compiler.py
```

After starting, the program will open the command menu in the selected language.

---

## 📜 Commands

| Command   | Description                                                 |
| --------- | ----------------------------------------------------------- |
| `/help`   | Show all available commands                                 |
| `/github` | Print the project GitHub link                               |
| `/start`  | Compile an existing `.pyx` file                             |
| `/create` | Create and compile a new `.pyx` file                        |
| `/import` | Create a `.py` file that imports the selected `.pyx` module |
| `/lan`    | Change the interface language                               |
| `/exit`   | Exit the program                                            |

---

## 🌐 Language Switch

The language is changed with the `/lan` command.

After typing `/lan`, the program will prompt you to choose a language.

---

## 💡 Dependencies

To use the compiler, install the required packages:

```bash
pip install cython setuptools
```

---

## ❤️ About

This project is actively developed, regularly updated, and improved with new features and refinements.
We would be very happy if you starred our repository ⭐

---

## 🇷🇺 Русская версия

**Интерактивный компилятор для проектов на Cython с поддержкой русского и английского языков.**
Создавайте, компилируйте и управляйте `.pyx` модулями прямо из терминала с удобной системой команд и понятным рабочим процессом.

---

## ✨ Возможности

* Интерактивное меню в терминале
* Компиляция существующих `.pyx` файлов
* Автоматическое создание новых `.pyx` файлов
* Генерация `.py` файлов для импорта `.pyx` модулей
* Поддержка английского и русского языков
* Простое переключение языка через `/lan`
* Удобная работа через консоль
* Постоянное развитие и обновления

---

## 📂 Структура проекта

```text
compiler.py
├── setup.py
├── CompilerFunction.py
└── languges.py
```

| Файл                  | Назначение                 |
| --------------------- | -------------------------- |
| `compiler.py`         | Запуск компилятора         |
| `setup.py`            | Интерфейс команд           |
| `CompilerFunction.py` | Основная логика компиляции |
| `languges.py`         | Строки интерфейса          |

---

## 🚀 Запуск

```bash
python compiler.py
```

После запуска программа откроет меню команд на выбранном языке.

---

## 📜 Команды

| Команда   | Описание                                                        |
| --------- | --------------------------------------------------------------- |
| `/help`   | Показать список доступных команд                                |
| `/github` | Вывести ссылку на GitHub проекта                                |
| `/start`  | Скомпилировать существующий `.pyx` файл                         |
| `/create` | Создать и скомпилировать новый `.pyx` файл                      |
| `/import` | Создать `.py` файл, который импортирует выбранный `.pyx` модуль |
| `/lan`    | Изменение языка                                                 |
| `/exit`   | Выйти из программы                                              |

---

## 🌐 Переключение языка

Язык задаётся при помощи команды `/lan`.

После ввода `/lan` появится поле ввода, где вам предложат выбрать язык.

---

## 💡 Зависимости

Для работы компилятора требуется установить нужные библиотеки:

```bash
pip install cython setuptools
```

---

## ❤️ О проекте

Проект активно развивается, регулярно обновляется и получает новые улучшения.
Мы будем очень рады, если вы поставите звезду нашему репозиторию ⭐
