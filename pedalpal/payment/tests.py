from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Payment
from authentication.models import Profile


class PaymentTestCase(APITestCase):
    def test_add_payment(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "amount": 2000,
        }
        response = self.client.post("/payment/add_payment/", data)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_update_balance(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "amount": 1000,
        }
        response = self.client.post("/payment/update_balance/", data)
        print(response.json())
        self.assertEqual(response.status_code, 200)

        data["amount"] = -1000
        response = self.client.post("/payment/update_balance/", data)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_balance(self):
        self.client.force_authenticate(user=self.user)
        data = {}
        response = self.client.get("/payment/get_balance/", data)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_transaction(self):
        self.client.force_authenticate(user=self.user)
        data = {}
        response = self.client.get("/payment/get_transactions/", data)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.user = Profile.objects.create(
            email="test@user.com",
            first_name="Test",
            last_name="User",
            phone="1234567890",
            password="test1234",
        )
