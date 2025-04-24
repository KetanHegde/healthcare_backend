# 🏥 Healthcare Backend API

A secure and scalable backend system for managing users, patients, doctors, and their relationships in a healthcare setting.

Built using **Django 5.2**, **Django REST Framework**, **PostgreSQL**, and **JWT Authentication**.

---

## 🔧 Technologies Used

- Django 5.2
- Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- Python Decouple (for environment variables)

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/healthcare_project.git
cd healthcare_project
```

2. **Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` File**
```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

5. **Apply Migrations and Run the Server**
```bash
python manage.py migrate
python manage.py runserver
```

---


## 📂 API Endpoints

### 👤 User Authentication
- `POST /api/auth/register/` — Register a new user
- `POST /api/auth/login/` — Login and receive JWT

### 🩺 Patient Management
- `POST /api/patients/` — Add a new patient (Auth required)
- `GET /api/patients/` — Retrieve patients of authenticated user
- `GET /api/patients/<id>/` — Get patient by ID
- `PUT /api/patients/<id>/` — Update patient
- `DELETE /api/patients/<id>/` — Delete patient

### 👨‍⚕️ Doctor Management
- `POST /api/doctors/` — Add a new doctor (Auth required)
- `GET /api/doctors/` — List all doctors
- `GET /api/doctors/<id>/` — Get doctor by ID
- `PUT /api/doctors/<id>/` — Update doctor
- `DELETE /api/doctors/<id>/` — Delete doctor

### 🔗 Patient-Doctor Mapping
- `POST /api/mappings/` — Assign a doctor to a patient
- `GET /api/mappings/` — Get all mappings
- `GET /api/mappings/<patient_id>/` — Get doctors for a patient
- `DELETE /api/mappings/delete/<id>/` — Remove a doctor from patient

---

## 🧪 Testing

- Use Postman or any API client.
- JWT required for all non-public endpoints.

---

## 📝 License

Licensed under the MIT License.