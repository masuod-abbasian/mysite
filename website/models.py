from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=250)
    email = models.EmailField()
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.name
