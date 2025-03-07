from django.urls import path, include
from .views import home_page, about_page
# endpoint -> urllar
urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
]
