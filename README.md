# Study Assistant — starter

A starter repository for the CSC10014 Smart Virtual Assistant project.

## Setup

1. Clone the repository:

```bash
git clone git@github.com:csc10014-team06/lab01-assistant-team06.git
```

2. Navigate to the project directory:

```bash
cd lab01-assistant-team06
```

3. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
# On Windows, use:
# .venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

## Run

```bash
python -m assistant "where is the library?"
# -> Library: room B.201, open Mon-Sat 07:00-20:00.
```

## Test

```bash
pytest -q
```

## Project structure

```text
lab01-assistant-team06/
├── README.md 
├── .gitignore requirements.txt pyproject.toml
├── src/assistant/
├── ui/README.md
├── data/README.md
├── tests/
├── docs/README.md docs/team.md
└── scripts/check_env.py
```
