from django.db import models
class Voter(models.Model):  # Renamed from User to avoid conflict
    username = models.CharField(max_length=255, unique=True)
    epic_number= models.IntegerField()  # Removed max_length
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'voters'
