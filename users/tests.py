from django.test import TestCase, Client
from django.urls import reverse_lazy
from users.models import CustomUser
from apartments.models import Apartment


class ApartmentTest(TestCase):
	"""Apartment object methods' tests"""

	def setUp(self):
		self.user = CustomUser.objects.create_user(email="test3@gmail.com", password="123")
		self.client.force_login(self.user)
		Apartment.objects.create(
			area=123,
			floor=123,
			status='active',
			price=123,
			building=123,
			state=""
		)

	def test_login_required(self):
		"""Test authentication requirement"""
		self.client.logout()
		response = self.client.get(reverse_lazy("list"))
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/?next='+reverse_lazy("list"))

	def test_list(self):
		"""Test Apartments list"""
		response = self.client.get(reverse_lazy("list"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'apartments.html')

	def test_create(self):
		"""Test Apartments create"""
		response = self.client.post(reverse_lazy("create"), data={
			"area": 123,
			"floor": 123,
			"status": 'active',
			"price": 123,
			"building": 123,
			"state": ""
		})
		self.assertEqual(response.status_code, 200)

	def test_update(self):
		"""Test Apartments update"""
		apartment = Apartment.objects.first()

		response = self.client.post(reverse_lazy("update", kwargs={"id": apartment.id}), data={
			"area": 100,
			"floor": 11000,
			"status": 'reserved',
			"price": 1200000,
			"building": "Magic City",
			"state": "reserved"
		})
