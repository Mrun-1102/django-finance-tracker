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
![register page](https://github.com/user-attachments/assets/2944aa79-043e-41b5-9fa3-0101d99f8c38)

![Login page](https://github.com/user-attachments/assets/9cbe4033-8df3-46c0-8897-b35919f0d03f)

![dashboard](https://github.com/user-attachments/assets/1681781d-7759-49ae-8f11-959742a8fdfe)

![income](https://github.com/user-attachments/assets/b8fa90ee-c3d4-4d12-b0b0-1e63e0bd597e)

![expense page](https://github.com/user-attachments/assets/1aa44b32-1fc6-41c5-8c35-13c4c403e9ed)

![visualizations](https://github.com/user-attachments/assets/cf8a3f27-a16b-40a9-a8c8-f3815060d9cb)

