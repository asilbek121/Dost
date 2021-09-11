from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('musix', views.musix, name="musix"),
    path('test', views.test, name="test"),

]