from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

# about, category, contact, blog, blog_detail, latest_news, main
def about_page(request):
    pass

