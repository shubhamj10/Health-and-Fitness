import unittest
class UserRegistration:
    def __init__(self):
        self.users = {}

    def register_user(self, email, password):
        if not email or not password:
            return "Email and password are required"

        if email in self.users:
            return "Email is already registered. Please log in or use a different email"

        self.users[email] = password
        return "Registration successful"


class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.reg = UserRegistration()

    def test_successful_registration(self):
        result = self.reg.register_user("test@example.com", "password123")
        self.assertEqual(result, "Registration successful")

    def test_duplicate_registration(self):
        self.reg.register_user("test@example.com", "password123")
        result = self.reg.register_user("test@example.com", "password456")
        self.assertEqual(result, "Email is already registered. Please log in or use a different email")

    def test_missing_fields_registration(self):
        result = self.reg.register_user("", "password123")
        self.assertEqual(result, "Email and password are required")

        result = self.reg.register_user("test@example.com", "")
        self.assertEqual(result, "Email and password are required")

if __name__ == '__main__':
    unittest.main()
