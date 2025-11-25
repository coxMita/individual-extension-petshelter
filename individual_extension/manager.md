## What Gets Created

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