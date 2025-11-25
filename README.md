# Smart Manufacturing Analytics System
University of Cincinnati – Capstone Project

## Overview
End-to-end analytics system for university enrollment and performance tracking. Includes data generation, ETL pipelines, data modeling in Postgres, automated workflows with Airflow, and interactive dashboards in Power BI.

## Features
- Automated data pipelines using Python and Airflow
- KPI dashboards for retention, GPA trends, and course demand
- Data quality checks and incremental refresh for reliable reporting

## Tools & Technologies
Python (pandas, SQLAlchemy), Postgres, Airflow, Power BI, SQL Server/Azure Data Factory

## Usage
1. Load CSVs into `data/`
2. Run `etl_pipeline.py` to load data into Postgres
3. Use `airflow_dag.py` to schedule automated ETL
4. Open Power BI dashboards
