

### Fully Automated

```bash
# 1. Create manager user
python setup_manager.py

# 2. Modify templates automatically
python modify_templates.py
```

### Option B: Manual Template Modification

```bash
# 1. Create manager user
python setup_manager.py

# 2. Follow instructions in TEMPLATE_MODIFICATIONS.md
#    to modify templates manually
```

## 📋 What Gets Created

A new user with these credentials:
- **Username:** manager
- **Password:** manager123
- **Email:** manager@manager.com
- **Role:** Staff (not superuser)

## ✅ Manager Capabilities

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

## ❌ Manager Limitations

The manager user will NOT be able to:
- Access Django Admin panel (`/admin/`)
- See "Django Admin" link in navigation
- Manage user accounts
- Change site-wide settings

## 🔧 Technical Details

### How It Works

The system uses Django's built-in user flags:

```python
# Admin user
is_staff = True
is_superuser = True

# Manager user
is_staff = True
is_superuser = False  # <-- Key difference

# Regular user
is_staff = False
is_superuser = False
```

### Permission Check

The existing view decorator allows both admins and managers:

```python
@user_passes_test(is_admin_user)
def admin_dashboard(request):
    # Both admins and managers can access this
    pass

def is_admin_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)
```

### Template Conditional

Templates check for superuser to show Django Admin link:

```django
{% if user.is_superuser %}
    <a href="/admin/">Django Admin</a>
{% endif %}
```

## 📁 Files Modified

The setup modifies these 6 template files:
1. `shelter/templates/shelter/admin/admin_dashboard.html`
2. `shelter/templates/shelter/admin/admin_applications.html`
3. `shelter/templates/shelter/admin/admin_application_detail.html`
4. `shelter/templates/shelter/admin/admin_pets.html`
5. `shelter/templates/shelter/admin/admin_contacts.html`
6. `shelter/templates/shelter/admin/admin_contact_detail.html`

**Change:** Wraps Django Admin link with `{% if user.is_superuser %}` condition

## 🧪 Testing

### Test as Manager
```
URL: http://localhost:8000/login/
Username: manager
Password: manager123

Expected:
✅ Can access /admin-dashboard/
✅ Can see Applications, Pets, Contacts
❌ Cannot see "Django Admin" link
❌ Cannot access /admin/ directly (will get permission error)
```

### Test as Admin
```
URL: http://localhost:8000/login/
Username: admin
Password: admin123

Expected:
✅ Can access /admin-dashboard/
✅ Can see Applications, Pets, Contacts
✅ Can see "Django Admin" link
✅ Can access /admin/
```

## 🔒 Security Considerations

### Default Password
The default password `manager123` is only for initial setup. You should:
1. Login as manager immediately after setup
2. Change password to something secure
3. Consider implementing forced password change on first login

### Direct Access Prevention
By default, managers might still access `/admin/` if they type the URL directly (they'll see limited features). To completely block this, add to `urls.py`:

```python
from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser

urlpatterns = [
    path('admin/', user_passes_test(is_superuser)(admin.site.urls)),
    # ...
]
```

### Best Practices
- Use strong, unique passwords
- Enable Django's password validation
- Implement session timeouts
- Log administrative actions
- Regular security audits

## 🛠️ Creating Additional Managers

### Using Django Shell
```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User

manager = User.objects.create_user(
    username='manager2',
    email='manager2@example.com',
    password='SecurePass123!',
    first_name='Second',
    last_name='Manager'
)
manager.is_staff = True
manager.is_superuser = False
manager.save()
```

### Using Admin Panel
1. Login as admin
2. Go to `/admin/auth/user/add/`
3. Create user with:
   - Desired username/email/password
   - Check "Staff status" ✅
   - Uncheck "Superuser status" ❌
4. Save

## 🐛 Troubleshooting

### Manager Sees Django Admin Link
**Problem:** Link is still visible in navigation  
**Solution:** 
- Verify all 6 templates were modified
- Check for syntax errors in templates
- Clear browser cache
- Restart Django server

### Manager Can't Access Dashboard
**Problem:** Gets permission denied  
**Solution:**
- Check `is_staff=True` in database
- Verify user exists: `User.objects.get(username='manager')`
- Check view decorators are correct

### Templates Not Updating
**Problem:** Changes don't appear  
**Solution:**
- Restart Django development server
- Clear browser cache (Ctrl+Shift+R)
- Check for template syntax errors
- Verify correct template directory

### Automated Script Fails
**Problem:** `modify_templates.py` reports errors  
**Solution:**
- Run from project root directory (where manage.py is)
- Check file paths are correct
- Verify templates exist
- Try manual modification instead

## 📖 Documentation

- **Quick Reference:** `QUICK_REFERENCE.md`
- **Setup Guide:** `MANAGER_SETUP_GUIDE.md`
- **Template Changes:** `TEMPLATE_MODIFICATIONS.md`

## 🆘 Support

If you encounter issues:

1. **Check logs:**
   ```bash
   python manage.py runserver
   # Watch console for errors
   ```

2. **Verify user in database:**
   ```bash
   python manage.py shell
   >>> from django.contrib.auth.models import User
   >>> m = User.objects.get(username='manager')
   >>> print(f"is_staff: {m.is_staff}")
   >>> print(f"is_superuser: {m.is_superuser}")
   ```

3. **Check template syntax:**
   ```bash
   python manage.py check --deploy
   ```

4. **Review documentation:**
   - Read through MANAGER_SETUP_GUIDE.md
   - Check TEMPLATE_MODIFICATIONS.md
   - Consult QUICK_REFERENCE.md

## 📝 Version History

- **v1.0** - Initial release
  - Manager user creation script
  - Automated template modification
  - Comprehensive documentation

## 📄 License

This is part of the PawHaven project and follows the same license.

## 👥 Contributing

If you find issues or have suggestions:
1. Document the problem
2. Include error messages
3. Describe expected vs actual behavior
4. Share your environment details

---

**Ready to get started?** Run `python setup_manager.py` now!