# 💰 Django Finance Tracker with AI Assistant

A powerful, full-stack personal finance application built with Django, TiDB, and Google Gemini AI. Track your income and expenses, visualize your spending patterns, and get personalized financial advice from an integrated AI.

## 📸 Dashboard Preview

![AI Finance Assistant Dashboard]

## 🚀 Features

- **Auth System**: Secure user registration and login with field-level validation and error reporting.
- **Finance Tracking**: Add, edit, and delete income and expense records.
- **Interactive Dashboard**:
  - Real-time Balance calculation.
  - **Category-wise Expense Pie Chart** (Chart.js) with robust resizing.
  - **Monthly Expense Trend Line Chart** (Chart.js) with automated data alignment.
- **AI Finance Assistant**: Integrated **Google Gemini 2.5 Flash** assistant that understands your spending data and provides intelligent, context-aware advice.
- **Budget Management**: Set monthly limits and get overspending alerts.
- **Data Export**: Export your financial data to CSV.

## 🛠️ Tech Stack

- **Backend**: Python / Django 5.x
- **Database**: TiDB (Distributed SQL) with SSL encryption
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 5, Chart.js
- **AI**: Google Gemini API (`google-genai` modern SDK)
- **Deployment**: WhiteNoise (Static files), Gunicorn (Production server)

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd django-finance-tracker
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root and add:
   ```env
   SECRET_KEY=your_django_secret
   DEBUG=True
   DATABASE_URL=your_tidb_connection_string
   GOOGLE_API_KEY=your_gemini_api_key
   ```

5. **Database Setup**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```
---
## 📸 Screenshots

### Registration Page
![Register](https://github.com/user-attachments/assets/2944aa79-043e-41b5-9fa3-0101d99f8c38)

### Login Page
![Login](https://github.com/user-attachments/assets/9cbe4033-8df3-46c0-8897-b35919f0d03f)

### Dashboard
![Dashboard](https://github.com/user-attachments/assets/1681781d-7759-49ae-8f11-959742a8fdfe)

### Income Management
![Income](https://github.com/user-attachments/assets/b8fa90ee-c3d4-4d12-b0b0-1e63e0bd597e)

### Expense Tracking
![Expenses](https://github.com/user-attachments/assets/1aa44b32-1fc6-41c5-8c35-13c4c403e9ed)

### Visualizations
![Charts](https://github.com/user-attachments/assets/cf8a3f27-a16b-40a9-a8c8-f3815060d9cb)

### AI Finance Assistant
![AI Assistant](https://github.com/user-attachments/assets/b4688a81-4efb-4ca0-94ba-a61a9c01625c) 
---

## 📊 Documentation

For detailed technical architecture, database design, and interview prep, see:
[Project Documentation](documentation.md)
