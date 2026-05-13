def create_profile(username, password):
    if len(password) < 8:
        return "Error: Password too short"
    return f"User {username} successfully securely created."
