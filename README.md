# Data Structure Filtering

## Project Description
This project reads employee records from JSON and CSV files, combines the data, filters active employees, and generates a summary audit report.

## Features
- Read data from JSON files.
- Read data from CSV files.
- Combine employee records.
- Filter active employees.
- Calculate average salary.
- Generate department-wise employee counts.
- Save the summary report as a JSON file.

## Technologies Used
- Python
- JSON
- CSV

## Project Structure
```text
Data_Structure_Filtering/
├── data/
│   ├── employees.json
│   └── employees.csv
├── output/
│   └── summary_audit.json
├── main.py
├── requirements.txt
└── .gitignore
```

## How to Run
```bash
python main.py
```

## Output
The program displays the total number of active employees, average salary, and department summary. It saves the audit report in `output/summary_audit.json`.

## Author
Afsana
