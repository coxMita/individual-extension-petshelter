# Pet Shelter Project

This repository contains **Individual extension made by Mihai-Adrian Briceag**:

## Folder Structure

```
individual-extension-petshelter/
├── individual_extension/  
└── README.md    
```

---

## Assignment 3 – Individual Extension

### Setup & Installation

1. Navigate to the project folder:

```bash
   cd individual_extension
```

2. Create a virtual environment (recommended):

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
   pip install -r requirements.txt
```

4. Run migrations:

```bash
   python manage.py migrate
```

### Running the Server

```bash
python manage.py runserver
```

Visit: http://localhost:8000

### User Access

- **Username:** `user`
- **Password:** `Password1.`

### Manager Access

- **Username:** `manager`
- **Password:** `manager123`
- **Role:** Staff (not superuser)

### Admin Access

- **URL:** http://localhost:8000/admin
- **Username:** `admin`
- **Password:** `admin123`
- **Role:** Superuser

---
