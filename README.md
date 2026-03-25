# Lab 1: Grade Evaluator & Archiver

How to Run the Python Script

1. Make sure `grades.csv` is in the same folder as `grade-evaluator.py`.
2. Run the script:
```
   python grade-evaluator.py
```
3. When prompted, type: `grades.csv`

## How to Run the Shell Script

1. Give the script execute permission (first time only):
```
   chmod +x organizer.sh
```
2. Run it:
```
   ./organizer.sh
```
   This will move `grades.csv` into the `archive/` folder with a timestamp,
   create a fresh empty `grades.csv`, and log the action to `organizer.log`.