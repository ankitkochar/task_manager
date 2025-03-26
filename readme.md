# Task Management API

This project is a Django-based Task Management API that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users. It also includes APIs to create and fetch user details.

## Features
- Create a user
- Get user details by ID
- Create a task
- Assign a task to one or multiple users
- Retrieve tasks assigned to a specific user

## Technologies Used
- Python 3
- Django
- Django REST Framework
- SQLite

---

## **Setup Instructions (Windows)**

### **Step 1: Clone the Repository**
```powershell
git clone https://github.com/ankitkochar/task_manager.git
cd task_manager
```

### **Step 2: Create and Activate Virtual Environment**
```powershell
python -m venv venv  # Create virtual environment
venv\Scripts\activate  # Activate virtual environment
```

### **Step 3: Install Dependencies**
```powershell
pip install django djangorestframework
```

### **Step 4: Apply Migrations**
```powershell
python manage.py makemigrations tasks
python manage.py migrate
```

### **Step 5: Run the Server**
```powershell
python manage.py runserver
```
Server will start at: `http://127.0.0.1:8000/`

---

## **API Endpoints**

### **1. Create a User**
- **Endpoint:** `POST /api/users/`
- **Payload:**
```json
{
  "name": "Abhishek Sharma",
  "email": "abhisharm123@gmail.com",
  "mobile": "9996479978"
}
```
- **Response:**
```json
{
  "id": 1,
  "name": "Abhishek Sharma",
  "email": "abhisharma123@gmail.com",
  "mobile": "9996479978"
}
```

---

### **2. Get User Details**
- **Endpoint:** `GET /api/users/{user_id}/`
- **Response:**
```json
{
  "id": 1,
  "name": "Abhishek Sharma",
  "email": "abhisharma123@gmail.com",
  "mobile": "9996479978"
}
```

---

### **3. Create a Task**
- **Endpoint:** `POST /api/tasks/`
- **Payload:**
```json
{
  "name": "New Task",
  "description": "Task description"
}
```
- **Response:**
```json
{
  "id": 1,
  "name": "New Task",
  "description": "Task description",
  "created_at": "2024-03-25T12:00:00Z",
  "status": "pending",
  "users": []
}
```

---

### **4. Assign Task to Users**
- **Endpoint:** `POST /api/tasks/{task_id}/assign/`
- **Payload:**
```json
{
  "users": [1, 2]
}
```
- **Response:**
```json
{
  "id": 1,
  "name": "New Task",
  "users": [1, 2]
}
```

---

### **5. Get Tasks Assigned to a User**
- **Endpoint:** `GET /api/users/{user_id}/tasks/`
- **Response:**
```json
[
  {
    "id": 1,
    "name": "New Task",
    "description": "Task description",
    "status": "pending"
  }
]
```

---