from django import template
from blog.models import POST

register = template.Library()

@register.inclusion_tag('website/latest-posts.html')
def index_latest_posts(arg=6):
    posts = POST.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}