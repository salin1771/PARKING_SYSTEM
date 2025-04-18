# 🅿️ Parking System API - Django Project

A full-stack backend project for managing parking operations using Django and Django REST Framework. This system is designed to handle vehicle entries/exits, track available slots, and provide API endpoints for all core operations. Built as part of a learning journey to master backend development, low-level design, and real-world Django applications.

---

## 🚀 Features

- 🏢 Supports multiple parking lots with different capacities
- 🚗 Entry & exit APIs for vehicles
- 🅿️ Dynamic slot allocation logic
- 📦 RESTful API endpoints using Django REST Framework
- 🔐 Admin panel to manage data
- 🧪 Easily testable and scalable architecture

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (can be switched to PostgreSQL/MySQL easily)
- **Language:** Python 3.9+
- **Tools:** Django Admin, DRF, Postman for API testing

---

## 📂 Project Structure

parking_system/ ├── api/ # API views and serializers ├── parking/ # Core models and logic ├── parking_system/ # Project settings and URLs ├── db.sqlite3 # Database ├── manage.py └── requirements.txt



---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/salin1771/parking-system-django.git
cd parking-system-django
2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies

pip install -r requirements.txt
4. Run migrations

python manage.py makemigrations
python manage.py migrate
5. Create superuser (for admin access)

python manage.py createsuperuser
6. Start the development server

python manage.py runserver
🔗 API Endpoints

Method	Endpoint	Description
POST	/api/entry/	Register vehicle entry
POST	/api/exit/	Register vehicle exit
GET	/api/slots/	Get available parking slots
GET	/api/vehicles/	List all parked vehicles
You can test all APIs using Postman or cURL.

🧠 How It Works
Each parking lot has a capacity.

When a vehicle enters, it is assigned the nearest available slot.

When it exits, the slot is marked as available again.

Admin can monitor vehicle activity and slot usage.

✅ To-Do
Add token authentication

Add unit and integration tests

Deploy to Heroku / Render

Add Swagger/OpenAPI documentation

🤝 Contributing
Open to suggestions and improvements! Feel free to fork, raise issues, or submit PRs.

📬 Contact
📧 salin488superfast@gmail.com
