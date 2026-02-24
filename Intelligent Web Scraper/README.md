# 🚀 Intelligent Web Data Pipeline
> **An end-to-end Python engine for dynamic API extraction, automated data cleaning, and professional reporting.**

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-data_cleaning-green.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-red.svg)

## 🌟 Overview
This project is a high-performance **ETL (Extract, Transform, Load)** pipeline designed to solve the problem of "dirty" web data. It intelligently inspects JSON/HTML structures, allows for selective data extraction, and prepares "Golden" datasets ready for business analysis.

---

## 🛠️ Key Features
* **🔍 Intelligent Ingestion:** Dynamically detects JSON structure (Dictionaries vs. Lists) and allows users to browse keys before saving.
* **🧹 Automated Cleaning Engine:** A robust Pandas-based transformation layer that:
    * Removes duplicate records.
    * Handles missing values (NaN) intelligently.
    * Standardizes whitespace and data types.
* **📊 Multi-Format Export:** Seamlessly merges new API data with existing local datasets in Excel and JSON formats.
* **⚡ Modern Architecture:** Built using `pathlib` for cross-platform file management and `tqdm` for real-time progress monitoring.

---

## 🏗️ Architecture Flow


1.  **Extract:** Fetching raw data from REST APIs via `Requests`.
2.  **Transform:** Applying data cleaning logic with `Pandas`.
3.  **Load:** Storing persistent records in `Excel` (`raw.xlsx` & `Cleaned_data.xlsx`).

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* MS Excel (for viewing outputs)

### Installation
1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/intelligent-web-scraper.git](https://github.com/yourusername/intelligent-web-scraper.git)
   cd intelligent-web-scraper
