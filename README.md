# Automobile-Sales-Interactive-Dashboard
This project is an interactive Dash and Plotly-based dashboard designed to explore and visualize historical automobile sales trends in the United States. It allows users to analyze how sales behavior changes across different years, months, vehicle types, and economic conditions such as recession periods.

⭐ Key Features

Two Analysis Modes

Yearly Statistics – Explore sales performance across selected years, monthly trends, and advertising expenditure distribution.

Recession Period Statistics – Visualize sales patterns during recession years, including:

Average sales over recession periods

Sales by vehicle type

Advertising expenditure per vehicle type

Effect of unemployment rate on sales

Fully Interactive UI

Dynamic dropdown menus for selecting report type and year

Automatic updates through Dash callbacks

Responsive chart layout with Plotly interactive graphs

Data Source

Dataset: Historical Automobile Sales

Hosted on IBM Cloud Object Storage

Loaded directly using pandas

📊 Visualizations Included

Line charts for sales trends

Bar charts for vehicle-type comparisons

Pie charts for advertising expenditure

Multivariate visuals showing relationships between sales and unemployment rate

🛠️ Tech Stack

Python

Dash (web framework)

Plotly Express (interactive visualizations)

Pandas (data manipulation)

▶️ How to Run

Install dependencies:

pip install dash plotly pandas


Run the application:

python app.py


Open your browser at:

http://127.0.0.1:8050/

🎯 Purpose

This dashboard provides an intuitive analytical tool for understanding market trends in the automobile industry. It is ideal for data analysts, students, or anyone interested in interactive data exploration using Dash.
