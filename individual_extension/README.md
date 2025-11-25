## What is new

A new user with these credentials:
- **Username:** manager
- **Password:** manager123
- **Email:** manager@manager.com
- **Role:** Staff (not superuser)

## Manager Capabilities

The manager user will be able to:
- Access Admin Dashboard (`/admin-dashboard/`)
- View and manage adoption applications
- Update application statuses
- Add notes to applications
- View and manage pets
- Edit pet information
- View contact messages
- Mark messages as read/responded
- Filter and search all data
- View dashboard statistics

## Manager Limitations

The manager user will NOT be able to:
- Access Django Admin panel (`/admin/`)
- See "Django Admin" link in navigation
- Manage user accounts
- Change site-wide settings

## Technical Details

The system uses Django's built-in user flags:

```python
# Admin user
is_staff = True
is_superuser = True

# Manager user
is_staff = True
is_superuser = False  

# Regular user
is_staff = False
is_superuser = False
```

The existing view decorator allows both admins and managers:

```python
@user_passes_test(is_admin_user)
def admin_dashboard(request):
    # Both admins and managers can access this
    pass

def is_admin_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)
```

Templates check for superuser to show Django Admin link:

```django
{% if user.is_superuser %}
    <a href="/admin/">Django Admin</a>
{% endif %}
```

## Files Modified

1. `shelter/templates/shelter/admin/admin_dashboard.html`
2. `shelter/templates/shelter/admin/admin_applications.html`
3. `shelter/templates/shelter/admin/admin_application_detail.html`
4. `shelter/templates/shelter/admin/admin_pets.html`
5. `shelter/templates/shelter/admin/admin_contacts.html`
6. `shelter/templates/shelter/admin/admin_contact_detail.html`

## Files Added
1. `shelter/templates/shelter/admin/admin_pet_edit.html`
2. `shelter/templates/shelter/admin/admin_pet_add.html`


# Previous Assignment PawHaven Pet Shelter - Django MVT Project

## 📁 Project Structure

```
pawhaven_project/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── db.sqlite3                        # SQLite database
├── pawhaven_project/                 # Main project folder
│   ├── settings.py                   # Project settings
│   ├── urls.py                       # Main URL configuration
│   └── wsgi.py                       # WSGI configuration
└── shelter/                          # Main Django app
    ├── models.py                     # Database models (Pet, Application, etc.)
    ├── views.py                      # View functions
    ├── urls.py                       # App URL patterns
    ├── admin.py                      # Django admin configuration
    ├── templates/shelter/            # HTML templates
    │   ├── base.html                 # Base template with header/footer
    │   ├── index.html                # Homepage
    │   ├── pets.html                 # Pet listing with filters
    │   ├── pet_detail.html           # Individual pet details
    │   ├── about.html                # About page
    │   ├── contact.html              # Contact form
    │   ├── adoption.html             # Adoption process info
    │   └── success.html              # Success stories
    ├── static/shelter/               # Static files
    │   ├── css/
    │   │   ├── style.css             # Main styles
    │   │   └── components.css        # Component styles
    │   ├── js/
    │   │   ├── main.js               # Main JavaScript
    │   │   └── search.js             # Search functionality
    │   └── images/                   # Image directories
    └── migrations/                   # Database migrations
```

## 🗄️ Database Models

### Pet Model

Stores all pet information with fields for:

- Basic info: name, breed, age, gender, size, color
- Description and personality traits (JSON field)
- Medical information: vaccinated, spayed/neutered, microchipped, special needs
- Images: up to 3 images per pet
- Status: available, pending, or adopted
- Adoption fee and arrival date
- Featured flag for homepage display

### AdoptionApplication Model

Handles adoption applications with:

- Applicant contact information
- Pet selection
- Housing and household information
- Previous pet experience
- Application status tracking

### ContactMessage Model

Stores contact form submissions

### SuccessStory Model

Stores adoption success stories with:

- Adopter information
- Story text and image
- Link to adopted pet

## How to Run the Project

### 1. Start the Development Server

```bash
cd /pet-shelterr/backend_project
python manage.py runserver
```

Then visit: `http://localhost:8000`

**Credentials:**

- Username: `user`
- Password: `Password1.`

### 2. Access the Admin Panel

URL: `http://localhost:8000/admin`

**Credentials:**

- Username: `admin`
- Password: `admin123`

In the admin panel, you can:

- Add/edit/delete pets
- View adoption applications
- Read contact messages
- Manage success stories
- Upload pet images

## Key Features Implemented

### Frontend (Templates)

✅ Homepage with featured pets and statistics
✅ Pet listing page with filters (type, size, special needs)
✅ Individual pet detail pages
✅ Contact form with database storage
✅ About page
✅ Adoption process information page
✅ Success stories page
✅ Responsive navigation
✅ Django messages for user feedback

### Backend (Views & Models)

✅ Database models for pets, applications, contacts, stories
✅ Class-based views for pet listing and detail
✅ Function-based views for forms
✅ Filter and search functionality
✅ Pagination for pet listings
✅ Related pets suggestions
✅ Stats counter on homepage

### Admin Interface

✅ Full CRUD operations for all models
✅ Custom admin panels with filters and search
✅ Organized fieldsets for better UX

## 📚 URL Structure

```
/                          → Homepage
/pets/                     → Pet listing with filters
/pet/<id>/<slug>/          → Individual pet detail
/about/                    → About page
/contact/                  → Contact form
/success-stories/          → Success stories
/adoption/                 → Adoption process info
/adoption/apply/           → General adoption application
/adoption/apply/<id>/      → Adoption application for specific pet
/admin/                    → Django admin panel
```

## Key Django Concepts Used

1. **Models:** Object-Relational Mapping (ORM) for database
2. **Views:**
   - Class-based views (ListView, DetailView)
   - Function-based views for forms
3. **Templates:**
   - Template inheritance (extends)
   - Template tags ({% url %}, {% static %})
   - Template filters (|date, |truncatewords)
4. **Forms:** Django's form handling and CSRF protection
5. **Admin:** Customized admin interface
6. **Static Files:** CSS, JavaScript, images
7. **Media Files:** User-uploaded content
8. **URL Routing:** Clean, semantic URLs

## What Was Converted

### From Static HTML to Django Templates:

- ✅ index.html → Dynamic homepage with database content
- ✅ pets.html → Filterable, paginated pet listing
- ✅ pet-detail.html → Dynamic pet detail pages
- ✅ about.html → Static info page
- ✅ contact.html → Form with database storage
- ✅ adoption.html → Static info page
- ✅ success.html → Dynamic success stories

### From JSON to Database:

- ✅ pets.json → Pet model with 7 sample records
- ✅ Static data → Dynamic, editable database content

### New Features Added:

- ✅ Admin interface for content management
- ✅ Contact form submissions storage
- ✅ Adoption application system
- ✅ Success stories management
- ✅ Server-side filtering and search
- ✅ Pagination
- ✅ Django messages for user feedback
