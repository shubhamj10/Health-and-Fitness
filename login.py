import unittest
import time
def login_user(email, password):
    # Assuming you have a data store (e.g., database) where user data is stored
    users = {
        "test@example.com": "password123"  # Replace with actual user data
    }

    if email in users and users[email] == password:
        return True
    else:
        return False

class TestLogin(unittest.TestCase):
    def test_successful_login(self):
        # Assuming the user exists in your data store (e.g., database)
        result = login_user("test@example.com", "password123")
        self.assertTrue(result)

    def test_invalid_credentials(self):
        # Assuming the user exists but with an incorrect password
        result = login_user("test@example.com", "wrong_password")
        self.assertFalse(result)

    def test_nonexistent_user(self):
        # Assuming the user does not exist in your data store
        result = login_user("nonexistent@example.com", "password123")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
