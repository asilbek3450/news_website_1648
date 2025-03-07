from django.shortcuts import render
from .models import News, Category, UserModel, Comment
from django.shortcuts import get_object_or_404

# Create your views here.
def home_page(request):
    yangiliklar = News.objects.all()
    kategoriyalar = Category.objects.all()
    context = {
        'yangiliklar': yangiliklar,
        'kategoriyalar': kategoriyalar
    }
    return render(request, 'index.html', context)


def about_page(request):
    return render(request, 'about.html')


def news_page(request):
    yangiliklar = News.objects.all()
    kategoriyalar = Category.objects.all()
    context = {
        'yangiliklar': yangiliklar,
        'kategoriyalar': kategoriyalar
    }
    return render(request, 'blog.html', context)


def news_detail(request, pk):
    yangilik = get_object_or_404(News, pk=pk)
    kategoriyalar = Category.objects.all()
    kommentariyalar = Comment.objects.filter(news_id=pk)
    context = {
        'yangilik': yangilik,
        'kategoriyalar': kategoriyalar,
        'comments': kommentariyalar
    }
    return render(request, 'news_detail.html', context)


def contact_page(request):
    return render(request, 'contact.html')