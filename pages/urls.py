# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, ContactUsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contactus/', ContactUsPageView.as_view(), name='contact us'),
]
