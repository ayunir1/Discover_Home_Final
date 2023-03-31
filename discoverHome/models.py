from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # participant form fields
    username = models.CharField(max_length=100)
    email = models.CharField(max_length = 250)
    password = models.CharField(max_length=150)

    class Meta:
        db_table = "user"