# Decorator
def check_admin(func):
    def wrapper(user):
        if user["role"] == "Admin":  # Only allow Admin users
            func(user)
        else:
            print("Access Denied: Admin role required.")
    return wrapper

# Restricted functions
@check_admin
def modify_settings(user):
    print(f"{user['name']} modified system settings.")

@check_admin
def update_software(user):
    print(f"{user['name']} updated the software.")


# Users
users = [
    {"name": "Kabir", "role": "Admin"},
    {"name": "Priya", "role": "User"}
]

# Test cases
modify_settings(users[0])  # Admin user
modify_settings(users[1])  # Non-Admin user
update_software(users[0])  # Admin user
update_software(users[1])  # Non-Admin user
check_admin(update_software)(users[1])