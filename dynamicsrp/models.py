"""
App Models
Create your models in here
"""

# Django
from django.db import models


class General(models.Model):
    """Meta model for app permissions"""

    class Meta:
        """Meta definitions"""

        managed = False
        default_permissions = ()
        permissions = (("basic_access", "Can access this app"),)

class Ship(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)
    ship_id = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.name

class Reimbursement(models.Model):
    index = models.IntegerField(default=0, unique=False)
    name = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return "#" + str(self.index) + " " + self.name

class Payout(models.Model):
    value = models.IntegerField(default=0, unique=False)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name="cells", default=1)
    reimbursement = models.ForeignKey(Reimbursement, on_delete=models.CASCADE, related_name="cells", default=1)

    def __str__(self):
        return "(" + self.reimbursement.name + ") " + self.ship.name + ": " + format(self.value, ",") + " ISK"

