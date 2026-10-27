# Reflection: Lab 5 Static Code Analysis

**Student:** Spoorthy M  
**SRN:** PES1UG24AM280

### 1. What did each tool help identify?

Pylint helped focus on maintainability problems such as mutable default arguments, unclear global state, and missing documentation. Bandit focused on security risks such as string-formatted SQL and unnecessary shell execution. Flake8 focused on consistency and readability, such as comparisons with `None` and long lines. Actual tool-specific results should be read from the generated reports.

### 2. Which problem was most serious, and why?

The string-formatted SQL query was the most important security issue because untrusted student or scheme strings could change the meaning of a database statement. Using SQLite parameter placeholders keeps user-supplied values separate from SQL code.

### 3. How did the fixes affect the program?

The updated version still creates scholarship awards, counts them by scheme, and disburses funds. It additionally prevents repeat disbursement of the same award, initializes a separate audit list for independent calls, avoids executing shell commands, and exposes a `main()` entry point that does not run automatically on import.

### 4. What did I learn from static analysis?

Different tools catch different categories of problems. A script that runs successfully can still contain security weaknesses, subtle bugs, and formatting issues. Running tools before and after changes gives evidence that fixes addressed warnings; running functional checks separately is important because static analysis alone cannot prove correct behavior.
