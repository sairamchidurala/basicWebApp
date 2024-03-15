from django.db import models


class User(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    date_of_birth = models.DateField()

    class Meta:
        app_label = 'users'
