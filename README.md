# static-code-analysis
# 🧮 Inventory Management System – Static Code Review Report

### 🧩 Static Code Analysis – Summary of Issues and Fixes

| Issue | Type | Line(s) | Description | Resolution |
|--------|------|----------|--------------|-------------|
| Mutable default argument | Logic | Old version | Used `logs=[]` as a default mutable value | Replaced with `None` and initialized within the function |
| Missing docstrings | Style | Multiple | Several methods lacked purpose and parameter descriptions | Added short but meaningful docstrings throughout the code |
| Naming convention | Convention | Multiple | Functions used `camelCase` style | Converted all to `snake_case` as per PEP8 |
| File handling | Maintainability | 64–70 | Used `open()` without encoding or context manager | Implemented `with open(..., encoding="utf-8")` for safety |
| Global variable usage | Design | 10 | Relied on `global stock_data` | Refactored to a class-based approach (`Inventory`) for encapsulation |
| Logging and feedback | Maintainability | 20–40 | Used `print()` for output | Replaced with structured logging for clarity and control |
| Dangerous function | Security | Old version | Contained `eval()` in main | Removed completely to prevent security risks |
| Exception handling | Reliability | Multiple | Bare except statements used | Updated with proper exception types and messages |
| Type checking | Robustness | 25–35 | Functions accepted invalid argument types | Added runtime validation and type hints |
| Unused imports | Cleanup | 2 | `logging` not used earlier | Properly configured logging and removed unused lines |

---

## 1️⃣ Which issues were easiest or hardest to fix, and why?

**Easiest:**  
Style-related issues like missing docstrings, inconsistent naming, and whitespace problems were quick to correct.  
These only required small edits or reformatting and were clearly pointed out by Pylint’s warnings.

**Hardest:**  
The most challenging fix was restructuring the code into a class format.  
This required changing how functions accessed shared data and ensuring the logic still worked correctly.  
Additionally, handling type validation without breaking the main logic needed careful debugging.

---

## 2️⃣ Did any of the static analysis results seem like false positives?

Yes — one example was the warning about avoiding global variables.  
While generally valid, the use of a global dictionary in the initial version was intentional for simplicity in a small script.  
Also, Pylint sometimes complained about missing return statements in helper functions that didn’t actually need to return anything — these weren’t real issues in this context.

---

## 3️⃣ How would you integrate static analysis tools into your normal workflow?

Static code analysis tools can easily be built into a development workflow using automation.  
For example:
- Add **Pylint**, **Flake8**, and **Bandit** checks in **GitHub Actions** or any CI/CD pipeline.  
- Use **pre-commit hooks** to block commits that fail code quality standards.  
- Enable **auto-linting in VS Code** so that warnings appear instantly while writing code.  

This ensures that code remains consistent, clean, and secure before merging or deploying changes.

---

## 4️⃣ What improvements were observed after applying the fixes?

After implementing all corrections:
- The code is now **object-oriented**, easier to extend, and safer.  
- **Logging** replaced raw prints, making debugging cleaner.  
- **Type hints** and **error handling** prevent unexpected crashes.  
- **Docstrings and PEP8 compliance** made the code far more readable and professional.  
- Removing unsafe calls (like `eval`) improved security.

Overall, the readability, reliability, and maintainability of the code improved significantly, and the final Pylint score increased from **~5.3 → 9.85+**, approaching perfect standards.

---

### ✅ Final Note

Even small codebases benefit from static analysis.  
This exercise showed how combining automated linting with careful refactoring can turn a basic script into clean, production-quality Python code.
