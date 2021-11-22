from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class POST(models.Model):
    image = models.ImageField(upload_to = 'blog/', default = 'blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    # tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(allow_unicode=True)
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return "{} - {}".format(self.title,self.id)

    

    # def snippets(self):
    #     return self.content[:100] + '...'