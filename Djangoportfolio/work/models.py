from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="work/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    views = models.PositiveIntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

