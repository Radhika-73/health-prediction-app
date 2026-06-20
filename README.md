# health-prediction-app
# 🏥 Health Prediction Application with AI-Powered Risk Analysis

A full-stack **Health Prediction Application** built using **Python**, **Streamlit**, and **SQLite**. The application allows healthcare staff to manage patient records and generate AI-powered health risk predictions based on blood test results such as Glucose, Haemoglobin, and Cholesterol levels.

---

# 📋 Project Overview

This application helps users:

* Store patient information securely
* Perform CRUD (Create, Read, Update, Delete) operations
* Validate user inputs
* Generate health risk predictions
* Manage patient records using a database
* Display prediction results in a user-friendly interface

The project demonstrates Python development, database management, data validation, and AI/ML integration concepts.

---

# ✨ Features

* 👤 Patient Registration
* 📊 Health Risk Prediction
* ➕ Add New Patient Records
* 📖 View Patient Records
* ✏️ Update Existing Records
* 🗑️ Delete Patient Records
* ✅ Input Validation
* 💾 SQLite Database Storage
* 🧠 AI-Based Health Analysis

---

# 🛠️ Tech Stack

| Component       | Technology               |
| --------------- | ------------------------ |
| Frontend        | Streamlit                |
| Backend         | Python                   |
| Database        | SQLite                   |
| Data Handling   | Pandas                   |
| AI/ML Logic     | Python Prediction Module |
| Version Control | Git & GitHub             |

---

# 📂 Folder Structure

```text
HealthPredictionApp/
│
├── app.py
├── database.py
├── predictor.py
├── health.db
├── requirements.txt
├── README.md
└── screenshots/
```

---

# 🔧 Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/Radhika-73/health-prediction-app.git

cd health-prediction-app
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas scikit-learn
```

---

# ▶️ Run Application

Execute:

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

Open this URL in your browser.

---

# 🗄️ Database Structure

Table Name:

```sql
patients
```

Columns:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
name TEXT
dob TEXT
email TEXT
glucose REAL
haemoglobin REAL
cholesterol REAL
remarks TEXT
```

---

# 📸 Application Modules

## ➕ Add Patient

Enter:

* Full Name
* Date of Birth
* Email Address
* Glucose Level
* Haemoglobin Level
* Cholesterol Level

The application generates a health prediction and stores all details in the database.

---

## 📖 View Patients

Displays all stored patient records in a tabular format.

---

## ✏️ Update Patient

* Select Patient ID
* Modify details
* Save changes

The prediction remarks are automatically recalculated.

---

## 🗑️ Delete Patient

* Select Patient ID
* Delete the patient record permanently

---

# 🧠 Prediction Logic

The application analyses:

* Glucose Level
* Haemoglobin Level
* Cholesterol Level

Example Rules:

| Condition         | Prediction            |
| ----------------- | --------------------- |
| Glucose > 140     | High Diabetes Risk    |
| Haemoglobin < 12  | Possible Anaemia      |
| Cholesterol > 200 | High Cholesterol Risk |

Example Output:

```text
High Diabetes Risk, Possible Anaemia, High Cholesterol Risk
```

---

# ✅ Validation Rules

### Email Validation

Valid:

```text
user@gmail.com
```

Invalid:

```text
usergmail.com
```

### Date Validation

Future dates are not allowed.

### Numeric Validation

Blood test values must be numeric and greater than zero.

---

# 🎯 Learning Outcomes

This project demonstrates:

* Python Programming
* Database Operations
* CRUD Functionality
* Data Validation
* Streamlit Application Development
* Healthcare Data Processing
* Basic AI/ML Prediction Logic
* GitHub Project Management

---

# 📬 Contact

Developer: Radhika Naganaboyina

Email : naganaboyinaradhika931@gmail.com

GitHub: https://github.com/Radhika-73

LinkedIn: linkedin.com/in/radhika-157624255

---

# 📄 License

This project was developed for educational and assessment purposes only.

