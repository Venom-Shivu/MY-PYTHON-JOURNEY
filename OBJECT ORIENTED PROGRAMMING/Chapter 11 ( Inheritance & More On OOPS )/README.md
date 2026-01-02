# Chapter 11: Inheritance & Advanced OOP

![Banner](https://img.shields.io/badge/Chapter_11-Inheritance_&_Advanced_OOP-blue?style=for-the-badge&logo=python&logoColor=white)

## 📌 Overview
This chapter covers **advanced Object-Oriented Programming concepts**, focusing on inheritance, polymorphism, and special Python methods.  
These concepts enable code reuse, extensibility, and more structured application design.

---

## 📚 Topics Covered

### 1. Inheritance
Inheritance allows a child class to reuse and extend the functionality of a parent class.

Types of inheritance:
- **Single** – One child, one parent  
- **Multiple** – One child, multiple parents  
- **Multilevel** – Inheritance across multiple levels  

---

### 2. The `super()` Method
- Used to access parent class methods and constructors
- Helps extend behavior without duplicating or overwriting logic

---

### 3. Class Methods & Static Methods
- **Class Methods (`@classmethod`)** operate on class-level data
- **Static Methods (`@staticmethod`)** provide utility functionality independent of class state

---

### 4. Property Decorators
- **`@property`** enables attribute-style access to methods
- **Setters** allow controlled updates and validation
- Improves encapsulation and data integrity

---

### 5. Operator Overloading & Dunder Methods
- Customizes object behavior using special methods
- Enables user-defined objects to behave like built-in types
- Common methods include `__add__`, `__str__`, and `__len__`

---

## ✅ Key Takeaways
- Inheritance supports code reuse and extensibility
- `super()` enables clean parent–child integration
- Decorators and dunder methods enhance class behavior
