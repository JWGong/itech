from django.test import TestCase
from unittest.mock import patch


class webTest(TestCase):
    def setUp(self):
        pass

    def test_login_with_wrong_password(self):
        data = {
            "username": "root",
            "password": "321"
        }
        res = self.client.post("/login/", data=data, content_type="application/x-www-form-urlencoded")
        self.assertEqual(res.status_code, 403)

    def test_register(self):
        data = {
            "username": "root9",
            "password": "321",
            "email": "1@1.co,",
            "first_name": "1",
            "last_name": "2"
        }
        res = self.client.get("/register/", data=data, content_type="application/x-www-form-urlencoded")
        self.assertEqual(res.status_code, 200)

    def test_home_page(self):
        res = self.client.get("/home/")
        self.assertEqual(res.status_code, 200)

    def test_dish_page(self):
        res = self.client.get("/dish?dId=10")
        self.assertEqual(res.status_code, 301)
