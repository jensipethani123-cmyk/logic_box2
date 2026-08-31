# Logic Box: Pattern Generator and Number Analyzer

**Author:** Jensi Pethani  
**Course/Project:** BCA Practical Assignment  

A Python-based menu-driven console application designed to practice control structures, loops (`for` and `while`), the `range()` function, and conditional statements.

## Project Objectives
* **Control Structures & Loops:** Implement nested loops and range iterations.
* **Menu-Driven Interface:** Provide an interactive console menu allowing users to choose between generating patterns, analyzing numbers, or exiting the program.
* **Logical Problem Solving:** Validate user inputs and execute mathematical/pattern algorithms efficiently.

---

## Features & Functionality

### 1. Pattern Generator
* Prompts the user to enter a positive row count.
* Utilizes nested loops to generate a clean **Right-angled triangle** pattern using asterisks (`*`).

### 2. Number Analyzer
* Prompts the user to enter a starting and ending range.
* Iterates through the given range using a `for` loop and the `range()` function to:
  * Check and display whether each number is **Odd** or **Even**.
  * Calculate and display the cumulative **Sum of all numbers** within the specified range.

### 3. Menu Options & Flow
* **1. Generate a Pattern:** Launches the pattern creation tool.
* **2. Analyze a Range of Numbers:** Launches the number analysis tool.
* **3. Exit:** Gracefully terminates the program loop.

---

## Example Console Interaction

```text
Welcome To the Pattern Generator and Number Analyzer!

Selected The Number
1. Generate a patten
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 1

--- Pattern Create ---
Enter the Number To create A pattern:-> 5
--- Generated Pattern ---
*
**
***
****
*****

Selected The Number
1. Generate a patten
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 2

--- Number Analyzer ---
Enter The Start Number To Start: 10
Enter The End Number To Stop: 15
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd
Sum of all numbers from 10 to 15 is: 75

Selected The Number
1. Generate a patten
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 3
Good Byee