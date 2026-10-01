# 🔐 Random Password Generator

## 📌 Overview

The **Random Password Generator** is a Python-based command-line application that generates random passwords according to user-defined requirements.

Users can choose the password length and select the character types they want to include, such as uppercase letters, lowercase letters, numbers, and symbols. The application also includes input validation and a password-generation limit.

## 🎯 Objective

The objective of this project is to develop a simple Python tool that can:

* Generate random passwords.
* Allow users to select the password length.
* Enforce a minimum password length of 8 characters.
* Allow users to select character types.
* Require at least two character types.
* Validate incorrect user input.
* Generate multiple passwords without restarting the program.
* Limit password generation to 10 times.
* Apply a 10-minute cooldown after reaching the limit.

## 🛠️ Technologies Used

* **Python 3**
* `random`
* `string`
* `time`

All modules used in this project are part of Python's standard library, so no external packages are required.

## ✨ Features

### 🔢 Custom Password Length

The user can enter the desired password length.

**Minimum length:** 8 characters.

### 🔤 Character Type Selection

The user can select one or more of the following:

```text
1. Uppercase Letters
2. Lowercase Letters
3. Numbers
4. Symbols
```

At least **two character types** must be selected.

### 🔐 Random Password Generation

The program generates a random password using the selected character types.

### ✅ Input Validation

The program validates:

* Password length
* Numeric input
* Minimum length requirement
* Character-type selection
* Invalid character choices
* Minimum two character types

### 🔄 Generate Multiple Passwords

Users can generate another password without restarting the application.

### ⏱️ Generation Limit

The application allows a maximum of **10 password generations**.

After 10 generations, the program starts a **10-minute cooldown** before allowing additional passwords.

Example:

```text
You have reached the maximum limit of 10 passwords.
Please wait 10 minutes before generating again.
```

## 💻 Example Output

```text
===== Random Password Generator =====

Enter password length (minimum 8): 12

Choose character types:
1. Uppercase letters
2. Lowercase letters
3. Numbers
4. Symbols

Enter choices (example: 1234): 1234

Generated Password: X7@kP2#mL9!Q

Passwords generated: 1/10

Generate another password? (yes/no): yes
```

## ❌ Example of Invalid Input

```text
Enter password length (minimum 8): 5

Error: Password length must be at least 8.
```

Another example:

```text
Enter choices (example: 1234): 1

Error: Select at least 2 character types.
```

## 📂 Project Structure

```text
Random-Password-Generator/
│
├── password_generator.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https:https://github.com/Nirliptasethy/Random_password_generator
```

### 2. Navigate to the project folder

```bash
cd Random Password Generator
```

### 3. Run the program

```bash
python Random_password_generator.py
```

No additional packages are required.

## 🧠 How It Works

The program follows these steps:

```text
Start
  ↓
Enter Password Length
  ↓
Validate Length
  ↓
Select Character Types
  ↓
Validate Selection
  ↓
Generate Random Password
  ↓
Display Password
  ↓
Generate Another?
  ↓
Yes → Repeat
No → Exit
  ↓
After 10 Generations
  ↓
10-Minute Cooldown
```

## 📚 Learning Outcomes

This project helped me practice:

* Python fundamentals
* Variables and data types
* `input()` and user interaction
* `if`, `elif`, and `else`
* `while` loops
* `try-except` exception handling
* String manipulation
* Random character generation
* Python standard libraries
* Input validation
* Timer and cooldown logic
* Command-line application development

## 🔮 Future Improvements

The project can be enhanced by adding:

* GUI using Tkinter
* Password strength indicator
* Copy-to-clipboard functionality
* Password history
* Customizable symbols
* Password saving functionality
* Secure password generation using Python's `secrets` module

## ⚠️ Security Note

This project is intended primarily for learning Python programming. For passwords used for real-world security, a cryptographically secure generator such as Python's `secrets` module is preferable to `random`.

## 👨‍💻 Project Information

**Project:** Random Password Generator
**Language:** Python
**Type:** Command-Line Application
**Level:** Beginner
**Status:** Completed
