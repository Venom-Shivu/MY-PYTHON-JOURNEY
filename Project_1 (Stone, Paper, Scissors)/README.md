
# 🎮 Stone, Paper, Scissors — Python Console Game

A command-line implementation of the classic **Stone, Paper, Scissors** game in Python.  
This project demonstrates **two different decision-making approaches**, progressing from readable conditional logic to an optimized mathematical solution.

---

## 📌 Project Overview

The game allows a user to play against the computer, which selects its move randomly using Python’s built-in `random` module.  
The project is designed to practice **conditional logic, randomness, input validation, and algorithmic optimization**.

---

## 🧠 Game Logic Approaches

### 🔹 Method 1: Conditional Logic (`if-elif-else`)
- Uses explicit conditions to compare user and computer choices  
- Prioritizes **readability and clarity**  
- Suitable for beginners learning control flow  

### 🔹 Method 2: Modular Arithmetic (Optimized)
- Represents moves numerically:
  - Rock = 0  
  - Paper = 1  
  - Scissors = 2  

- Determines the winner using:

```python
(computer_choice - user_choice) % 3
````

* Eliminates long conditional chains
* Demonstrates **efficient and scalable decision logic**

---

## ✨ Features

* User vs Computer gameplay
* Randomized computer choice
* Input validation for safe execution
* Clean, structured code
* Replay support (in enhanced version)
* Two alternative logic implementations

---

## 🚀 How to Run

### Prerequisites

Ensure Python 3 is installed:

```bash
python --version
```

### Run the Game

```bash
python game.py
```

---

## 🎯 Game Rules

* **Stone** beats **Scissors**
* **Paper** beats **Stone**
* **Scissors** beat **Paper**
* Same choice results in a **Tie**

---

## 📂 File Structure

```text
Stone-Paper-Scissors/
├── game.py
├── game_shortcut_method.py
└── README.md
```

---

## 📚 Learning Outcomes

This project helps reinforce:

* Conditional statements
* Random number generation
* Input validation
* Modular arithmetic for logic optimization
* Writing clean, maintainable Python code

---

## 📜 License

This project is intended for **educational and practice purposes**.


---

