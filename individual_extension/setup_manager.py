"""
Setup script for creating a Manager user in PawHaven

This script will:
1. Create a manager user with the specified credentials
2. Display instructions for template modifications

Run this script from your Django project root:
    python setup_manager.py
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawhaven_project.settings')
django.setup()

from django.contrib.auth.models import User


def create_manager_user():
    """Create the manager user"""
    print("=" * 70)
    print("PAWHAVEN MANAGER USER SETUP")
    print("=" * 70)
    print()
    
    # Check if manager already exists
    if User.objects.filter(username='manager').exists():
        print("⚠️  Manager user already exists!")
        manager = User.objects.get(username='manager')
        print(f"   Username: {manager.username}")
        print(f"   Email: {manager.email}")
        print(f"   is_staff: {manager.is_staff}")
        print(f"   is_superuser: {manager.is_superuser}")
        print()
        
        response = input("Do you want to update the existing manager user? (yes/no): ")
        if response.lower() != 'yes':
            print("Setup cancelled.")
            return
        
        # Update existing user
        manager.email = 'manager@manager.com'
        manager.set_password('manager123')
        manager.is_staff = True
        manager.is_superuser = False
        manager.first_name = 'Manager'
        manager.last_name = 'User'
        manager.save()
        print("✅ Manager user updated successfully!")
    else:
        # Create new manager user
        manager = User.objects.create_user(
            username='manager',
            email='manager@manager.com',
            password='manager123',
            first_name='Manager',
            last_name='User'
        )
        
        # Set staff status but NOT superuser
        manager.is_staff = True
        manager.is_superuser = False
        manager.save()
        print("✅ Manager user created successfully!")
    
    print()
    print("Manager User Credentials:")
    print("-" * 70)
    print(f"   Username: {manager.username}")
    print(f"   Password: manager123")
    print(f"   Email: {manager.email}")
    print(f"   is_staff: {manager.is_staff}")
    print(f"   is_superuser: {manager.is_superuser}")
    print()


def show_template_instructions():
    """Display instructions for template modifications"""
    print("=" * 70)
    print("TEMPLATE MODIFICATIONS REQUIRED")
    print("=" * 70)
    print()
    print("You need to modify the following template files to hide the Django")
    print("Admin link for managers. Replace the Django Admin link sections with")
    print("the conditional version shown below:")
    print()
    print("-" * 70)
    print()
    
    templates_to_modify = [
        'shelter/templates/shelter/admin/admin_dashboard.html',
        'shelter/templates/shelter/admin/admin_applications.html',
        'shelter/templates/shelter/admin/admin_application_detail.html',
        'shelter/templates/shelter/admin/admin_pets.html',
        'shelter/templates/shelter/admin/admin_contacts.html',
        'shelter/templates/shelter/admin/admin_contact_detail.html',
    ]
    
    print("Files to modify:")
    for template in templates_to_modify:
        print(f"   • {template}")
    print()
    print("-" * 70)
    print()
    print("FIND this code in each template:")
    print()
    print("    <a href=\"/admin/\" class=\"nav-item\">")
    print("        <span class=\"nav-icon\">⚙️</span>")
    print("        Django Admin")
    print("    </a>")
    print()
    print("REPLACE with:")
    print()
    print("    {% if user.is_superuser %}")
    print("    <a href=\"/admin/\" class=\"nav-item\">")
    print("        <span class=\"nav-icon\">⚙️</span>")
    print("        Django Admin")
    print("    </a>")
    print("    {% endif %}")
    print()
    print("-" * 70)
    print()


def show_completion_message():
    """Display completion message"""
    print("=" * 70)
    print("SETUP COMPLETE")
    print("=" * 70)
    print()
    print("The manager user has been created. Here's what you need to know:")
    print()
    print("✅ Manager user created with credentials:")
    print("   - Username: manager")
    print("   - Password: manager123")
    print("   - Email: manager@manager.com")
    print()
    print("✅ Manager has access to:")
    print("   - Admin Dashboard (/admin-dashboard/)")
    print("   - Manage Applications")
    print("   - Manage Pets")
    print("   - Contact Messages")
    print()
    print("❌ Manager does NOT have access to:")
    print("   - Django Admin Panel (/admin/)")
    print()
    print("📝 Next steps:")
    print("   1. Make the template modifications shown above")
    print("   2. Test login with manager credentials")
    print("   3. Verify manager can access dashboard but not /admin")
    print()
    print("=" * 70)
    print()


def main():
    try:
        create_manager_user()
        show_template_instructions()
        show_completion_message()
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Make sure you're running this from your Django project root")
        print("directory (the same directory as manage.py)")


if __name__ == '__main__':
    main()