# Teen-Mental-Health-Analyzer

# 🧠 Teen Mental Health: Automated EDA Pipeline

This repository contains an **Automated Exploratory Data Analysis (EDA)** script designed to analyze a Teen Mental Health dataset. 

Instead of generating charts manually, this Python script acts as an automated data analyst. Upon execution, it reads the raw dataset, processes the data using Pandas, generates key analytical charts using Matplotlib, and exports the visualizations as ready-to-use PNG reports.

## 📊 Data Source
The raw dataset used in this project is obtained from Kaggle:
[https://www.kaggle.com/datasets/algozee/teenager-menthal-healy/data]

## 📁 Project Structure
```text
├── data/
│   └── Teen_Mental_Health_Dataset.csv   # Raw dataset
├── reports/                             # Auto-generated analytical charts (PNG)
├── src/
│   └── report_generator.py              # Main visualization pipeline
└── README.md
```

✨ Key Features & Visualizations
Automated Directory Management: Automatically creates export folders (/reports) if they do not exist.

Platform Usage Analysis (Bar Chart): Analyzes the average daily social media hours per platform.

Sleep Impact Analysis (Scatter Plot): Visualizes the correlation between screen time before sleep and total sleep hours.

Stress Distribution (Histogram): Shows the distribution of stress levels among teens.