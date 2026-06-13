# OOP Cybersecurity Quiz Engine

A modular, terminal-based quiz application built in Python using advanced Object-Oriented Programming (OOP) architectures, clean encapsulation, and type inference.

![Python](https://img.shields.io/badge/Language-Python%203.8+-blue?logo=python&logoColor=white)
![Type System](https://img.shields.io/badge/Typing-Generics%20%2F%20Inference-orange)
![Design Pattern](https://img.shields.io/badge/Architecture-OOP%20%2F%20Decoupled-blue)
![Security Focus](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Data Format](https://img.shields.io/badge/Data-JSON-lightgrey?logo=json&logoColor=white)
![IDE](https://img.shields.io/badge/IDE-VS%20Code-blue?logo=visual-studio-code&logoColor=white)

---

## 📍 Quick Navigation
* [🌐 Engine Overview](#-engine-overview)
* [📦 System Architecture](#-system-architecture)
* [✨ Key Architecture Features](#-key-architecture-features)
* [📁 Repository Structure](#-repository-structure-and-module-index)
* [🛠️ Tech Stack](#️-tech-stack)
* [💻 System Requirements](#-system-requirements)
* [🚀 Setup & Execution Guide](#-setup--execution-guide)
* [📊 Performance Matrix](#-performance-matrix)
* [🏗️ Architectural Highlights](#%EF%B8%8F-architectural-highlights)

---

## 🌐 Engine Overview

The OOP Cybersecurity Quiz Engine is a type-safe, terminal-driven evaluation platform designed to process complex datasets without relying on runtime exception trapping. By utilizing structural type generics, custom iterator pools, and strong enum mapping, the application decouples data parsing from performance tracking while enforcing absolute internal state isolation.

---

## 📦 System Architecture


```text
                                ┌─────────────────────────────────────────────────────────────┐
                                │                    DATA INGESTION LAYER                     │
                                ├─────────────────────────────────────────────────────────────┤
                                │                       quiz_data.json                        │
                                │             (Strict Structured JSON Question Bank)          │
                                └──────────────────────────────┬──────────────────────────────┘
                                                               ↓
                                ┌─────────────────────────────────────────────────────────────┐
                                │                  GENERIC ENGINE INTERNALS                   │
                                ├────────────┬─────────────┬────────────┬─────────────┬───────┤
                                │ Generic[T] │ __repo /    │ SessionPool│ input filter│Grade  │
                                │  Data      │ __score     │  Custom    │             │Tier   │
                                │ Ingestion  │(Encapsulated│  Iterator  │ (`isdigit()`)│Enums │
                                │  Binds     │ Private Var)│  Override  │   Safety    │Metrics│
                                └────────────┴─────────────┴────────────┴─────────────┴───────┘
                                                               ↓
                                ┌─────────────────────────────────────────────────────────────┐
                                │                  PERFORMANCE OUTPUT METRIC                  │
                                ├─────────────────────────────────────────────────────────────┤
                                │                     Terminal Console stdout                 │
                                └─────────────────────────────────────────────────────────────┘

```

## ✨ Key Architecture Features
✅ Type Inference & Generics (Generic[T]) - Uses generic type binds to abstract the structure of the incoming data payload.

✅ Strict Encapsulation - Protects internal application states using pseudo-private attributes (__repository, __score).

✅ Custom Iterators - Implements a custom SessionPool class overriding __iter__ to loop through questions cleanly.

✅ Enum-Driven Metrics - Maps percentages to strongly-typed GradeTier enums rather than hardcoded string primitives.

✅ Defensive Coding - Completely avoids try-except blocks by utilizing boolean metrics checks (os.access, os.path.getsize) and input filters (isdigit()).

## 📁 Repository Structure and Module Index
The project codebase is organized into the following logical components:

### Core Processing Modules
quiz_app.py - Core OOP quiz engine logic containing class definitions, state controllers, and text parsing routines.

### Data Ecosystems
quiz_data.json - Decoupled dataset containing 50 cybersecurity conceptual validation records.

### Documentation
README.md - Structural user handbook and deployment technical implementation manual.

## 🛠️ Tech Stack

| Component | Technology | Quick Links |
| :--- | :--- | :--- |
| **Core Language** | Python 3.8+ (Standard Library Distribution) | [python.org](https://www.python.org/) |
| **Type Abstracting** | `typing.Generic`, `TypeVar`, `List` Type-Hinting | [Python Typing Docs](https://docs.python.org/3/library/typing.html) |
| **Data Parsing** | Native `json` Serialization/Deserialization Engine | [Python JSON Docs](https://docs.python.org/3/library/json.html) |
| **State Enumeration** | `enum.Enum` (Strongly-Typed Performance Classes) | [Python Enum Docs](https://docs.python.org/3/library/enum.html) |
| **Defensive I/O** | `os.path` Verification and Access Boundary Checkers | [Python OS Docs](https://docs.python.org/3/library/os.html) |

## 💻 System Requirements
Ensure your execution environment adheres to the following baseline parameters:

### Operating System: Cross-platform deployment (Windows 10/11, macOS, or Linux).

### Python Engine: Python 3.8+ with standard typing extensions enabled.

### Hardware Profiles: Ultra-lightweight footprint (Fully processes under 32MB system RAM overhead).

## 🚀 Setup & Execution Guide
### Step 1: Ingest Data (quiz_data.json)
Save your 50-question array as quiz_data.json in your working execution directory. Ensure each object follows this exact strict structure:

```JSON
{
  "question": "What flag is used in Nmap to enable service version detection?",
  "options": ["-sS", "-sV", "-O", "-A"],
  "answer": "-sV"
}
```
### Step 2: Verify File Tree Hierarchy
Ensure your local project directory matches the structural map layout below:
```Bash
quiz_core/
├── quiz_app.py
├── quiz_data.json
└── README.md
```
### Step 3: Run the Engine (quiz_app.py)
Execute the generic core engine terminal loop from your active console shell instance:
```Bash
python3 quiz_app.py
```

## 📊 Performance Matrix
The system dynamically processes final evaluation percentages directly into strongly-typed tracking buckets rather than utilizing loose strings:

| Accuracy Range | Enum Tier Class | System Status String | Evaluation Result |
| :---: | :---: | :---: | :---: |
| **$\ge$ 90%** | `GradeTier.ELITE` | `L33T / Elite Engineer` | **[Pass]** |
| **$\ge$ 75%** | `GradeTier.SENIOR` | `Senior Engineer` | **[Pass]** |
| **$\ge$ 50%** | `GradeTier.ASSOCIATE` | `SysAdmin / Associate` | **[Pass]** |
| **< 50%** | `GradeTier.REMEDIATION` | `Remediation Recommended` | **[Fail]** |



## 🏗️ Architectural Highlights
### 🔀 Generic Type Decoupling
By loading structures into abstract objects via Generic[T], the underlying quiz framework doesn't care about the domain model. The data layout can shift from cybersecurity domains to network topology mapping without altering memory state architectures.

## 🔐 Private Attribute Defense Matrix
Score metrics tracking variables match pseudo-private signature configurations (self.__score). This setup uses name-mangling protocols inside the Python compiler to prevent external calling modules from modifying execution states or altering score histories mid-session.

## 🎮 Pure Boolean Validation Loops
The code avoids expensive runtime exceptions by performing rigorous system state checks. File sizing assessments confirm resource footprints are greater than zero before parsing streams, and input capture logic applies character validation filters (isdigit()) before data meets the logic engine.

## 📄 License & Terms
This project is open-source. Feel free to copy, modify, and redistribute the modular quiz application framework as required.

