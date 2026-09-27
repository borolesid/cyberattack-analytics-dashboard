# 🛡️ Cyberattack Analytics Dashboard
**India Cyber Threat Intelligence Dashboard | Big Data Analysis Project**

---

## 📖 Project Overview

The Cyberattack Analytics Dashboard is a comprehensive Big Data Analysis project developed to analyze and visualize cyberattack data in India for the period 2023–2025.

The project processes large-scale cyberattack records and presents them through a premium, interactive Streamlit dashboard. It allows security analysts and users to identify attack patterns across different years, months, states, cities, attack categories, and subtypes.

## 🚀 Technologies Used

- **Python**: Core programming language
- **PySpark**: For distributed big data processing, cleaning, and aggregation
- **Pandas**: For lightweight data manipulation in the presentation layer
- **Streamlit**: For the interactive web application interface
- **Plotly**: For advanced, responsive data visualization
- **Parquet**: For efficient, columnar data storage of processed analytical results
- **Power BI**: For supplementary business intelligence and reporting

## 🗄️ Dataset Attributes

The underlying dataset tracks critical cyberattack information:
- **Year** & **Month**
- **Type of Attacks** (Broad classification)
- **Subtype** (Specific threat vector)
- **State** & **City** (Geographic origin/target)
- **Counts of Attack**

## ⚙️ Big Data Processing Architecture

1. **NCRP Data Extraction**
2. **PySpark Processing Engine**
   - Data Cleaning & Transformation
   - Distributed Data Aggregation
   - Generation of distinct analytical cubes (Year-wise, Month-wise, State-wise, Type-wise, City-wise)
3. **Parquet Storage Optimization**
4. **Streamlit Presentation Layer**
5. **Interactive Data Visualization**

## 🖥️ Dashboard Layout & Features

The dashboard features a professional dark cybersecurity-themed UI (with glassmorphism elements, neon accents, and responsive design) divided into specific analytical zones:

- **🔎 Explore Cyberattack Data**: Global filters for Year, State, and Attack Type.
- **📌 Key Performance Indicators**: High-level metrics for Total Attacks, Total States, Attack Types, and Dataset Records.
- **📊 Attack Overview**: High-level summary of attacks by year and attack type distribution.
- **🌍 Regional Threat Analysis**: Interactive India geographic map mapping threat concentration alongside the top 5 most attacked states.
- **📅 Temporal Analysis**: Chronological monthly attack trend analysis.
- **🔍 Attack Pattern Analysis**: Evolution of specific attack types by year and by month.
- **🏙️ Subtype & City Analysis**: Deep dive into the top 15 specific attack vectors and the most targeted cities.
- **📅 State-wise Year Analysis**: Detailed breakdown of state vulnerabilities across different years.
- **💡 Automated Cyberattack Insights**: Dynamically calculated observations summarizing the highest attack state, city, type, and temporal peaks.
- **📋 Data Explorer**: Full detailed data table with the ability to download the filtered results as a CSV.

## 🛠️ How to Run

1. Clone or download the repository.
2. Activate your Python virtual environment (e.g., `venv\Scripts\activate` on Windows).
3. Ensure all dependencies are installed from `requirements.txt`.
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
5. The dashboard will automatically open in your web browser.

---
*Project Period: 2023–2025*