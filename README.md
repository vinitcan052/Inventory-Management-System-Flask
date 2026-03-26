📦 Inventory Management System (Flask)

A modular and scalable Inventory Management System built using Flask, SQLAlchemy, and MySQL. This project follows a clean layered architecture (API → Service → DAO → DB) and supports authentication, product management, and inventory tracking.

🚀 Features
🔐 User Authentication (JWT-based)
📦 Product Management (CRUD operations)
📊 Inventory Tracking
🧩 Modular Architecture (Blueprints + Service Layer)
🌐 CORS enabled for frontend integration
🗄️ MySQL Database with SQLAlchemy ORM
🏗️ Project Structure
Inventory Management System Flask/
│
├── main.py                  # Application entry point
├── requirements.txt         # Dependencies
├── Procfile                 # Deployment config (Gunicorn)
│
└── app/
    ├── api/                 # Route handlers (Blueprints)
    │   ├── auth.py
    │   ├── product.py
    │   └── inventory.py
    │
    ├── services/            # Business logic layer
    │   ├── user_service.py
    │   ├── product_service.py
    │   └── inventory_service.py
    │
    ├── dao/                 # Data Access Layer
    │   ├── user_dao.py
    │   └── product_dao.py
    │
    ├── models/              # Database models
    │   └── models.py
    │
    ├── db/                  # DB session/engine setup
    │   └── session.py
    │
    ├── core/                # Core utilities (e.g., security)
    │   └── security.py
    │
    └── api/                 # Config / env / schema files
        ├── .env
        ├── db_schema.txt
        └── app.txt
⚙️ Tech Stack
Backend: Flask
ORM: SQLAlchemy
Database: MySQL
Authentication: JWT (PyJWT + bcrypt)
Deployment: Gunicorn
Environment Management: python-dotenv
🧑‍💻 Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/inventory-management-flask.git
cd inventory-management-flask
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables

Create a .env file inside app/:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=inventory_db
SECRET_KEY=your_secret_key
5️⃣ Run the application
python main.py

App will run on:

http://127.0.0.1:5000/
📡 API Endpoints
🔐 Auth
POST /auth/register
POST /auth/login
📦 Products
GET    /products/
POST   /products/
PUT    /products/<id>
DELETE /products/<id>
📊 Inventory
GET    /inventory/
POST   /inventory/
🧠 Architecture Overview

This project uses a layered architecture:

API Layer (Blueprints): Handles HTTP requests
Service Layer: Business logic
DAO Layer: Database queries
Model Layer: ORM entities

This separation improves:

Maintainability
Testability
Scalability
🚀 Deployment

Using Gunicorn:

gunicorn main:app

Or via Procfile (for platforms like Heroku):

web: gunicorn main:app
📌 Future Improvements
Role-based access control (RBAC)
Frontend integration (React / Angular)
Pagination & filtering
Dockerization
Unit & integration tests
🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

📄 License

This project is licensed under the MIT License.