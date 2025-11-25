"""
Automated Template Modifier for Manager User Setup

This script automatically modifies all admin template files to hide
the Django Admin link from managers.

Run from project root:
    python modify_templates.py
"""

import os
import re


def modify_template(filepath):
    """Modify a single template file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already modified
        if '{% if user.is_superuser %}' in content and 'Django Admin' in content:
            return 'ALREADY_MODIFIED'
        
        # Pattern to find Django Admin link
        pattern = r'(<a href="/admin/" class="nav-item">.*?<span class="nav-icon">⚙️</span>.*?Django Admin.*?</a>)'
        
        # Check if pattern exists
        if not re.search(pattern, content, re.DOTALL):
            return 'NOT_FOUND'
        
        # Replace with conditional version
        replacement = r'{% if user.is_superuser %}\n                    \1\n                    {% endif %}'
        modified_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Backup original file
        backup_path = filepath + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Write modified content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        return 'SUCCESS'
        
    except FileNotFoundError:
        return 'FILE_NOT_FOUND'
    except Exception as e:
        return f'ERROR: {str(e)}'


def main():
    print("=" * 70)
    print("AUTOMATED TEMPLATE MODIFIER FOR MANAGER USER SETUP")
    print("=" * 70)
    print()
    
    # Template files to modify
    templates = [
        'shelter/templates/shelter/admin/admin_dashboard.html',
        'shelter/templates/shelter/admin/admin_applications.html',
        'shelter/templates/shelter/admin/admin_application_detail.html',
        'shelter/templates/shelter/admin/admin_pets.html',
        'shelter/templates/shelter/admin/admin_contacts.html',
        'shelter/templates/shelter/admin/admin_contact_detail.html',
    ]
    
    print("⚠️  WARNING: This script will modify your template files!")
    print("Backups will be created with .backup extension.")
    print()
    
    # Confirm
    response = input("Do you want to proceed? (yes/no): ")
    if response.lower() != 'yes':
        print("Operation cancelled.")
        return
    
    print()
    print("-" * 70)
    print("Modifying templates...")
    print("-" * 70)
    print()
    
    results = {
        'SUCCESS': [],
        'ALREADY_MODIFIED': [],
        'NOT_FOUND': [],
        'FILE_NOT_FOUND': [],
        'ERROR': []
    }
    
    for template in templates:
        print(f"Processing: {template}...", end=" ")
        result = modify_template(template)
        
        if result.startswith('ERROR'):
            results['ERROR'].append((template, result))
            print(f"❌ {result}")
        elif result == 'SUCCESS':
            results['SUCCESS'].append(template)
            print("✅ Modified successfully")
        elif result == 'ALREADY_MODIFIED':
            results['ALREADY_MODIFIED'].append(template)
            print("ℹ️  Already modified")
        elif result == 'NOT_FOUND':
            results['NOT_FOUND'].append(template)
            print("⚠️  Django Admin link not found")
        elif result == 'FILE_NOT_FOUND':
            results['FILE_NOT_FOUND'].append(template)
            print("❌ File not found")
    
    print()
    print("-" * 70)
    print("SUMMARY")
    print("-" * 70)
    print()
    
    if results['SUCCESS']:
        print(f"✅ Successfully modified: {len(results['SUCCESS'])} file(s)")
        for f in results['SUCCESS']:
            print(f"   - {f}")
        print()
    
    if results['ALREADY_MODIFIED']:
        print(f"ℹ️  Already modified: {len(results['ALREADY_MODIFIED'])} file(s)")
        for f in results['ALREADY_MODIFIED']:
            print(f"   - {f}")
        print()
    
    if results['NOT_FOUND']:
        print(f"⚠️  Pattern not found: {len(results['NOT_FOUND'])} file(s)")
        print("   These files may have different structure or already modified manually")
        for f in results['NOT_FOUND']:
            print(f"   - {f}")
        print()
    
    if results['FILE_NOT_FOUND']:
        print(f"❌ Files not found: {len(results['FILE_NOT_FOUND'])} file(s)")
        print("   Make sure you're running this from the project root directory")
        for f in results['FILE_NOT_FOUND']:
            print(f"   - {f}")
        print()
    
    if results['ERROR']:
        print(f"❌ Errors: {len(results['ERROR'])} file(s)")
        for f, err in results['ERROR']:
            print(f"   - {f}: {err}")
        print()
    
    # Backup info
    if results['SUCCESS']:
        print("💾 Backups created:")
        print("   Original files saved with .backup extension")
        print("   To restore: mv file.backup file")
        print()
    
    print("-" * 70)
    print()
    
    # Next steps
    total_modified = len(results['SUCCESS']) + len(results['ALREADY_MODIFIED'])
    if total_modified == len(templates):
        print("✅ All templates processed successfully!")
        print()
        print("Next steps:")
        print("1. Restart your Django server")
        print("2. Login as manager (username: manager, password: manager123)")
        print("3. Verify the Django Admin link is not visible")
        print("4. Login as admin to verify the link is still visible for admins")
    else:
        print("⚠️  Some templates were not modified.")
        print("Please check the summary above and modify manually if needed.")
        print("See TEMPLATE_MODIFICATIONS.md for manual instructions.")
    
    print()
    print("=" * 70)


if __name__ == '__main__':
    main()