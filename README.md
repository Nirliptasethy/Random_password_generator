# Random_password_generator
# 🔐 Random Password Generator

## 📌 Project Overview

The **Random Password Generator** is a beginner-friendly Python command-line application that generates random and customizable passwords based on user-selected requirements.

The program allows users to choose the password length and character types, including uppercase letters, lowercase letters, numbers, and symbols. It also validates user input and allows multiple passwords to be generated without restarting the program.

To control repeated generation, the application allows a maximum of **10 password generations** before applying a **10-minute cooldown period**.

## 🎯 Objective

The main objective of this project is to build a Python tool that can:

* Generate random passwords.
* Allow users to specify password length.
* Enforce a minimum password length of 8 characters.
* Allow selection of different character types.
* Require at least 2 character types.
* Validate invalid user input.
* Generate multiple passwords in one session.
* Limit password generation to 10 times.
* Apply a 10-minute waiting period after reaching the limit.

## 🛠️ Technologies Used

* **Python 3**
* `random`
* `string`
* `time`

## ✨ Features

### 1. Custom Password Length

Users can specify the desired password length.

```text
Minimum length: 8 characters
```

### 2. Character Type Selection

Users can select from:

```text
1. Uppercase letters
2. Lowercase letters
3. Numbers
4. Symbols
```

At least **2 character types** must be selected.

### 3. Random Password Generation

The program uses Python's `random` module to generate passwords from the selected character sets.

### 4. Input Validation

The application checks for:

* Password length below 8
* Non-numeric password length
* Invalid character-type selections
* Fewer than 2 selected character types

### 5. Password Generation Limit

Users can generate a maximum of **10 passwords** in one session.

After reaching the limit:

```text
You have reached the maximum limit of 10 passwords.
Please wait 10 minutes before generating again.
```

The program then starts a **10-minute cooldown**.

### 6. Generate Another Password

Users can generate another password without restarting the program.

## 💻 Example

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

## 📂 Project Structure

```text
Random-Password-Generator/
│
├── password_generator.py
└── README.md
```

## 🚀 How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/Nirliptasethy/Random-password-generator.git
```

### Step 2: Open the project folder

```bash
cd random-password-generator
```

### Step 3: Run the program

```bash
python password_generator.py
```

No external packages are required because `random`, `string`, and `time` are built-in Python modules.

## 📚 What I Learned

Through this project, I practiced:

* Python loops
* Conditional statements
* User input handling
* Input validation
* Exception handling
* String manipulation
* Random value generation
* Using Python built-in modules
* Working with timers and delays
* Creating a command-line application

## 🔮 Future Improvements

Possible future enhancements include:

* Graphical User Interface (GUI)
* Copy password to clipboard
* Password strength indicator
* Password history
* Custom symbol selection
* Secure password generation using Python's `secrets` module
* Save generated passwords securely

## ⚠️ Security Note

This project is primarily designed for learning Python programming. For passwords intended for real-world security, a cryptographically secure generator such as Python's `secrets` module should be preferred over `random`.

## 👨‍💻 Project Type

**Beginner Python Project — Command-Line Application**
