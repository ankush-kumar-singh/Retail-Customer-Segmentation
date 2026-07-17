# 🛍️ Retail Customer Analytics Dashboard
### End-to-End Customer Segmentation using RFM Analysis & Interactive Dash Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Dash](https://img.shields.io/badge/Dash-Plotly-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-success)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Project Overview

This project performs **Customer Segmentation** using **RFM (Recency, Frequency, Monetary) Analysis** on a real-world UK retail dataset.

The project includes the complete analytics pipeline:

- Data Cleaning
- Feature Engineering
- RFM Score Calculation
- Customer Segmentation
- Exploratory Data Analysis
- Interactive Business Dashboard using Dash

The dashboard enables businesses to understand customer purchasing behaviour and identify valuable customer groups for targeted marketing.

---

# Dashboard Preview

## Dashboard Home

![Dashboard Home](images/dashboard_images/dashboard%201st%20page.png)

---

## Customer Behaviour Analysis

![Dashboard Analysis](images/dashboard_images/dashboard%202nd%20page.png)

---

## Customer Value & Correlation Analysis

![Dashboard Analysis](images/dashboard_images/dashboard%203rd%20page.png)

---

# Project Workflow

```
Raw Retail Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
RFM Calculation
        │
        ▼
Customer Segmentation
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Interactive Dash Dashboard
```

---

# Customer Segments

The customers are divided into the following business segments:

- Champions
- Loyal Customers
- Potential Loyalists
- New Customers
- Regular Customers
- Hibernating
- Lost Customers
- At Risk

Each segment is identified using RFM score combinations.

---

# Dashboard Features

### KPI Cards

- Total Customers
- Total Revenue
- Average Customer Value
- Champions Count

---

### Interactive Filters

- Segment Filter
- Customer Filter

---

### Visualizations

- Customer Distribution
- Segment Share
- RFM Bubble Plot
- Monetary Distribution
- Top Customers
- Correlation Heatmap

---

# Technologies Used

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Plotly
- Dash
- Dash Bootstrap Components

### Data Visualization

- Plotly Express
- Plotly Graph Objects

---

# Dataset

The project uses the **Online Retail Dataset (UK)**.

Main features include:

- Invoice
- Customer ID
- Invoice Date
- Quantity
- Unit Price
- Country

After preprocessing, the final dataset contains:

- Customer ID
- Recency
- Frequency
- Monetary
- Segment

---

# Folder Structure

```
Retail-Customer-Segmentation/
│
├── dashboard/
│   ├── app.py
│   ├── callbacks.py
│   ├── charts.py
│   ├── components.py
│   ├── data.py
│   └── theme.py
│
├── datasets/
│   ├── rfm_main.csv
│   ├── rfm.csv
│   ├── online_retail_rfm_working_data.csv
│   └── ...
│
├── images/
│   ├── dashboard_images/
│   │   ├── dashboard 1st page.png
│   │   ├── dashboard 2nd page.png
│   │   └── dashboard 3rd page.png
│   │
│   └── notebook_images/
│       ├── Average Monetary Value by Segment.png
│       ├── Average Purchase Frequency.png
│       ├── Average Recency.png
│       ├── Customer Segment Treemap.png
│       ├── Monetary Distribution.png
│       ├── Percentage Distribution.png
│       ├── Top 10 Spenders.png
│       └── ...
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_RFM_Analysis.ipynb
│   ├── 03_dashboard.ipynb
│   └── ...
│
└── README.md
```

---

# Business Insights

Some key findings from the analysis:

- Champions generate the highest revenue.
- Lost Customers represent the largest customer segment.
- Frequency and Monetary value show a strong positive relationship.
- Customers with low Recency tend to spend significantly more.
- RFM segmentation helps identify customers requiring retention strategies.

---

# Future Improvements

- Authentication System
- PDF Report Export
- Excel Report Export
- Predictive Customer Churn Model
- Customer Lifetime Value Prediction
- Recommendation Engine
- SQL Database Integration
- Cloud Deployment

---

# Author

**Ankush Kumar Singh**

Data Science | Machine Learning | Data Analytics

GitHub:
https://github.com/ankush-kumar-singh

LinkedIn:
www.linkedin.com/in/ankush-kumar-singh-04bb78243

---
⭐ If you found this project useful, consider giving it a star.