from django.db import models

# Create your models here.
class POST(models.Model):
    # image
    # author
    title = models.CharField(max_length=250)
    content = models.TextField()
    # category
    # tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return "{} - {}".format(self.title,self.id)