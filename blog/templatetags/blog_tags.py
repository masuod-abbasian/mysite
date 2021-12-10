from django import template
from blog.models import POST,Comment
from blog.models import Category
register = template.Library()

@register.simple_tag(name="totalposts")
def function():
    posts = POST.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="comments_count")
def function(pid):
    return Comment.objects.filter(post = pid,approved=True).count()

@register.simple_tag(name="posts")
def function():
    posts = POST.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + "..."

@register.inclusion_tag('blog/blog-popular-post.html')
def latestposts(arg=2):
    postes = POST.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'postes':postes}

@register.inclusion_tag('blog/blog-category.html')
def postcategory():
    posts = POST.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories': cat_dict}


