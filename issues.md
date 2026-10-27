# Lab 5: Identified Issues and Fixes

Student: Spoorthy M  |  SRN: PES1UG24AM280

These findings are based on inspection of the assigned source. Actual tool findings and ratings must be checked against the generated reports.

| Issue | Type / tool | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| SQL string formatting | Security / Bandit | 9 | Student and scheme values directly inserted into an SQL statement; SQL injection risk | Use `?` placeholders and bind parameters |
| Shell execution | Security / Bandit | 26 | `os.system()` executes a shell command unnecessarily | Replace with database commit and a normal `print` |
| Mutable default argument | Correctness / Pylint | 8 | Default audit list persists across independent calls | Use `audit=None` and create a fresh list inside |
| Broad exception + silent pass | Quality / Pylint | 27-28 | Catches everything and silently hides failure | Remove unnecessary exception handler |
| Global mutable counter | Design / Pylint | 17 | State outside functions is hard to reason about | Return disbursed amount and track results in `main()` |
| Repeat disbursement | Logic | 19-23 | Same award could be paid twice | Check existing `disbursed` flag before updating |
| None comparison | Style / Flake8 | 32 | `== None` violates PEP 8 | Change to `is None` |
| Non-snake-case name | Style / Pylint | 31 | `bySchemeCount` does not use Python naming convention | Rename to `by_scheme_count` |
| Long code lines | Style / Flake8 | 5, 9, 18, 34 | Statements exceed the usual 79-character limit | Split SQL into wrapped strings and expressions |
| Unconditional `main()` call | Quality / Pylint | 44 | Demo runs when module is imported | Add `if __name__ == "__main__":` guard |

## Git commits

The local Git repository contains the original baseline and three separate fix commits, one each for Bandit, Pylint, and Flake8. The baseline commit is retained to make the before/after audit reproducible.
