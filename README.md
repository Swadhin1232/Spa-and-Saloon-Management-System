💇‍♀️ Spa and Salon Management System (Django)

📌 Project Overview


The Spa and Salon Management System is a web-based application built using Django that helps manage salon operations such as appointments, customers, staff, and billing efficiently.

---

🚀 Features

👤 Customer Management

- User registration & login (authentication system)
- Profile management
- View booking history

📅 Appointment System

- Book appointments online
- Check staff availability
- Cancel/reschedule bookings

💼 Staff Management

- Add/manage staff members
- Assign roles and schedules
- Track availability

💰 Billing System

- Generate invoices
- Track payments
- Service-wise billing

🧾 Service Management

- Add/edit/delete services
- Set service pricing
- Categorize services

📊 Admin Dashboard

- View analytics & reports
- Monitor bookings and revenue
- Manage users and staff

---

🛠️ Technologies Used

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default) / MySQL
- Other Tools: Django Admin Panel

---

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/salon-management-system.git
cd salon-management-system

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Linux/Mac

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser

python manage.py createsuperuser

6️⃣ Run the Server

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/

---

📂 Project Structure

SalonManagement/
│── salon/                # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
│── templates/
│── static/
│── db.sqlite3
│── manage.py

---

🗂️ Database Models (Basic)

Customer

- name
- email
- phone

Staff

- name
- role
- availability

Service

- name
- price
- duration

Appointment

- customer (ForeignKey)
- staff (ForeignKey)
- service (ForeignKey)
- date & time
- status

---

🔐 User Roles

- Admin: Full control via Django Admin
- Staff: Manage appointments
- Customer: Book services

---

📸 Screenshots

(Add your project screenshots here)

---

📈 Future Enhancements

- Online payment integration (Razorpay/Stripe)
- Email/SMS notifications
- REST API (Django REST Framework)
- Mobile app integration

---

👨‍💻 Author

- Your Name

---

📜 License

This project is licensed under the MIT License.

---
