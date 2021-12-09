from django.contrib.sitemaps import Sitemap
from blog.models import POST
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return POST.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date

    # def location(self,item):
    #     return reverse('blog:single' ,kwargs={'pid':item.id})