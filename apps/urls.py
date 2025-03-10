from django.urls import path
from .views import home_page, about_page, news_page, news_detail, contact_page
# endpoint -> urllar
urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('news/', news_page, name='news'),
    path('news/<int:pk>/', news_detail, name='news-detail'),
    path('contact/', contact_page, name='contact'),
       
]
