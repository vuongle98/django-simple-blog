from django.shortcuts import render
from django.views import View
from .models import Category, Post
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
class Index(View):
    def get(self, request):
        categories = Category.objects.all()
        posts = Post.objects.filter(status=1).order_by('created_at')
        paginator = Paginator(posts, 2)

        page = request.GET.get('page')
        try:
            posts = paginator.get_page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmtyPage:
            posts = paginator.page(paginator.num_pages)

        data = {'posts': posts}
        return render(request, 'blog/index.html', data)

class Detail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/detail.html', {'post': post})