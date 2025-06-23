# 💰 Personal Finance Tracker

A full-stack Django web application that helps users manage their income, expenses, and monthly budgets — all while providing real-time visual insights.

---

## 📌 Features

- ✅ User Authentication (Login/Logout)
- 💵 Add, update, and delete **Income** and **Expenses**
- 📅 Set and monitor a **Monthly Budget**
- 🚨 Alerts for **Overspending**
- 📊 Visualizations using **Chart.js** (Pie & Line Charts)
- 📁 Export data as **CSV reports**
- 💻 Responsive UI with **Bootstrap 5**

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Charts**: Chart.js
- **Deployment**: Render (compatible with PythonAnywhere, Clever Cloud)

---



## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker

```
### 2️⃣ Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

```
### 3️⃣ Configure MySQL Database
Update the settings.py file with your MySQL credentials:
```bash 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate

```
### 5️⃣ Create Superuser
```bash
python manage.py createsuperuser

```
### 6️⃣ Run the Development Server
```bash
python manage.py runserver

```
Open your browser and visit:
http://127.0.0.1:8000/


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

