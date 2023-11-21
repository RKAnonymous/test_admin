from django.db import models
from users.models import CustomUser


APARTMENT_STATUSES = (
	('active', 'active'),
	('reserved', 'reserved'),
	('sold', 'sold'),
	('installment', 'installment'),
	('barter', 'barter'),
)

APARTMENT_BUILDINGS = (
	("Prime City", "Prime City"),
	("Kochmon", "Kochmon"),
	("Baytik", "Baytik"),
	("Magic City", "Magic City"),
)


class Apartment(models.Model):
	area = models.FloatField()
	floor = models.IntegerField()
	status = models.CharField(choices=APARTMENT_STATUSES, max_length=20, default='active')
	state = models.CharField(max_length=255, null=True, blank=True)
	price = models.FloatField()
	building = models.CharField(choices=APARTMENT_BUILDINGS, max_length=50)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)


class BookingApartment(models.Model):
	apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
