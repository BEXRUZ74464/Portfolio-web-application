from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    subject = models.CharField(max_length=110)
    text = models.TextField()

    def __str__(self):
        return self.name