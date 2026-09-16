# 🧩 Pattern Generator and Number Analyzer

An interactive Python console application designed to demonstrate control structures, loops, conditional statements, and arithmetic processing through a menu-driven program.

## Author
* **Jensi Pethani**
* **Course/Project:** Python Practical Assignment

## 🎯 Project Objectives
* **Menu-Driven Interface:** Continuously run a console menu allowing users to choose multiple operations until they decide to exit.
* **Pattern Generation:** Dynamically generate custom star patterns based on user-defined row counts using nested loops.
* **Number Analyzer:** Process a range of numbers (from start to end) to check and display whether each number is even or odd, while calculating their cumulative sum.

## ✨ Features & Functionality
1. **Interactive Menu System:**
   * Choice 1: Generate a star pattern (`*`) based on rows.
   * Choice 2: Analyze a range of numbers (Even/Odd checker and sum calculator).
   * Choice 3: Exit the application gracefully.

2. **Pattern Creator Feature:**
   * Validates that the entered number of rows is greater than 0.
   * Uses nested `for` loops to print a clean, incremental right-angled triangle star pattern.

3. **Number Analyzer Feature:**
   * Accepts a start number and an end number from the user.
   * Iterates through the given range, checking divisibility by 2 (`i % 2 == 0`) to classify each number as Even or Odd.
   * Accumulates and displays the total sum of all numbers in the specified range.

## 💻 Technologies Used
* Python 3
* Visual Studio Code
* Git & GitHub

## 📚 Concepts Covered
* `while True` infinite loops & break statements
* Conditional statements (`if`, `elif`, `else`)
* Nested loops (`for` loops inside `for` loops)
* Arithmetic and modulus operations (`%`, `+=`)
* User input handling and type casting (`int`)
* Formatted strings (`f-strings`) for clean console output

## 📂 Project Structure
```text
logic_box2/
│
├── pattern_analyzer.py
└── README.md

🖥️ Sample Console Output
Welcome To the Pattern Generator and Number Analyzer!

Selected The Number
1. Generate a patten
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 1

--- Pattern Create ---
Enter the Number To create A pattern:-> 4
--- Generated Pattern ---
 * 
 *  * 
 *  *  * 
 *  *  *  * 

Selected The Number
1. Generate a patten
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 2

--- Number Analyzer ---
Enter The Start Number To Start: 1
Enter The End Number To Stop: 3
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Sum of all numbers from 1 to 3 is: 6

Selected The Number
1. Generate a patten
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 3
Good Byee!