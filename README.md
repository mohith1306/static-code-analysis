# 🧮 Inventory Management System – Static Code Review Report

### 🧩 Static Code Analysis – Summary of Issues and Fixes

| Issue | Type | Line(s) | Description | Resolution |
|--------|------|----------|--------------|-------------|
| Function and Naming Conventions | Style | Multiple | Functions used `camelCase` and lacked docstrings | Renamed to `snake_case` and added concise docstrings following PEP8 |
| File & Exception Handling | Maintainability | 60–80 | Used plain `open()` and bare `except` blocks | Added `with open(..., encoding="utf-8")` and specific exception handling |
| Global and Structural Design | Logic | 10–40 | Relied on a global dictionary for data | Refactored into a class (`Inventory`) with methods and encapsulated data |
| Unsafe / Invalid Code Usage | Security | 85 | Contained `eval()` and weak input validation | Removed `eval()` and added type checking with warnings via logging |

---

## 1️⃣ Which issues were easiest or hardest to fix, and why?

**Easiest:**  
The easiest fixes were related to style — such as converting names to `snake_case`, adding docstrings, and cleaning up spacing. These were mostly formatting improvements identified directly by Pylint.

**Hardest:**  
The toughest change was refactoring the global-based logic into a class structure. This required rewriting how data was shared and accessed across functions, testing the logic again, and ensuring file operations still worked correctly after the change.

---

## 2️⃣ Did any of the static analysis results seem like false positives?

Yes — Pylint raised a few warnings that weren’t necessarily real issues in this context.  
For instance, it flagged the removal of global variables and the handling of missing keys as warnings, even though the simplified script design intentionally allowed these for demonstration purposes.

---

## 3️⃣ How would you integrate static analysis tools into your normal workflow?

Static analysis can be part of every stage of development:
- Use **Pylint** and **Flake8** checks through **GitHub Actions** to prevent poor-quality commits.  
- Set up **pre-commit hooks** to automatically reject code with linting errors.  
- Enable **live linting in IDEs (like VS Code)** to catch problems while coding.  

This helps enforce consistent coding standards and maintain high-quality, secure code throughout development.

---

## 4️⃣ What improvements were observed after applying the fixes?

After applying all changes:
- The code now follows **PEP8** standards, making it cleaner and easier to read.  
- **Logging** replaced `print()` statements, improving traceability.  
- **Error handling** and **type checks** prevent runtime issues.  
- The removal of `eval()` and global data increased safety and structure.  

As a result, the overall maintainability and reliability improved, and the Pylint score rose from **~5.3 → 9.85+**, approaching a perfect score.

---

### ✅ Final Reflection

Static analysis proved invaluable in identifying subtle issues beyond syntax — from naming consistency to better design patterns.  
These changes not only improved the score but also demonstrated how structured feedback can guide cleaner, professional-grade code development.
