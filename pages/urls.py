from django.urls import path
from .views import HomePageView, ContactView, AboutView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]
