from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    all_blogs = Blog.objects.order_by('-post_date')[:5]
    return render(request, 'blog/all_blogs.html', {
        'creator': 'Rilson Almeida',
        'blogs': all_blogs,
        })
    
    
def detail_blog(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {
        'creator': 'Rilson Almeida',
        'blog': detail_blog,
        })    