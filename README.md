# Updated_json_quiz

```markdown
# OOP Cybersecurity Quiz Engine
A modular, terminal-based quiz application built in Python using advanced Object-Oriented Programming (OOP) architectures, clean encapsulation, and type inference.
---
## Key Architecture Features
* **Type Inference & Generics (`Generic[T]`):** Uses generic type binds to abstract the structure of the incoming data payload.
* **Strict Encapsulation:** Protects internal application states using pseudo-private attributes (`__repository`, `__score`).
* **Custom Iterators:** Implements a custom `SessionPool` class overriding `__iter__` to loop through questions cleanly.
* **Enum-Driven Metrics:** Maps percentages to strongly-typed `GradeTier` enums rather than hardcoded string primitives.
* **Defensive Coding:** Completely avoids `try-except` blocks by utilizing boolean metrics checks (`os.access`, `os.path.getsize`) and input filters (`isdigit()`).
---
## Project Structure
```text
quiz_core/
├── quiz_app.py        # Core OOP quiz engine logic
├── quiz_data.json     # Decoupled dataset containing 50 questions
└── README.md          # Project handbook
```
## Setup & Execution
### 1. Ingest Data (quiz_data.json)
Save your generated 50-question array as quiz_data.json in your working directory. Ensure each object follows this schema:
```json
{
  "question": "What flag is used in Nmap to enable service version detection?",
  "options": ["-sS", "-sV", "-O", "-A"],
  "answer": "-sV"
}
```
### 2. Run the Engine (quiz_app.py)
Save the generic engine code into quiz_app.py and execute it from your terminal:
```bash
python3 quiz_app.py
```
## Performance Matrix
The system dynamically processes scores into the following evaluation tracking tiers:

| Accuracy Range | Enum Tier Class | Status |
| :--- | :--- | :--- |
| **\ge 90%** | GradeTier.ELITE | L33T / Elite Engineer [Pass] |
| **\ge 75%** | GradeTier.SENIOR | Senior Engineer [Pass] |
| **\ge 50%** | GradeTier.ASSOCIATE | SysAdmin / Associate [Pass] |
| **< 50%** | GradeTier.REMEDIATION | Remediation Recommended [Fail] |

```
```