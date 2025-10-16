# Zoitechk - Python Test


## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone hhttps://github.com/IamThejus/Django-Test.git
cd Django-Test
```

💾 Project Structure
```
myproject/
├── api/                     # Your Django app
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── myproject/               # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── __init__.py
├── api_tester.py            # ✅ Your test script
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3
```
2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   
```
On Windows
# or
```
source venv/bin/activate  
```
# On macOS/Linux
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Run Migrations
```
python manage.py migrate
```
5️⃣ Run the Development Server
```
python manage.py runserver
```
Then visit:
👉 http://127.0.0.1:8000/

🧠 API Endpoints
🧍 User Registration
```
POST /register/
```
Register a new user with validation.

Request

```
{
  "username": "thejus123",
  "email": "thejus@example.com",
  "password": "password123"
}
```
Response
```

{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "thejus123",
    "email": "thejus@example.com"
  }
}
```
👥 User Management

Method	Endpoint	Description
```
GET	/users/	Get all users
GET	/users/<id>/	Get user by ID
DELETE	/users/<id>/delete/	Delete user by ID
```

💰 Expense Tracker
Models
```
Category → name

Expense → title, amount, category, date

Summary Endpoint
GET /expenses/summary/
Returns total expense amount grouped by category.
```

Example Response
```
{
  "Food": 1200,
  "Travel": 3000,
  "Entertainment": 800
}
```
🧩 Tech Stack
```
Python 3.x

Django 4+

Django REST Framework

SQLite (default)
```


🧑‍💻 Author
```
Thejus Asokan
B.Tech CSE | APJ Abdul Kalam Technological University
Email: thejusasokan123@gmail.com
```

