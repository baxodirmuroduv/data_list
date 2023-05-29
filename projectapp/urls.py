from django.urls import path
from .views import HomePView, AboutPView, ContactPView

urlpatterns = [
    path('', HomePView.as_view(), name='home'),
    path('about/', AboutPView.as_view(), name='about'),
    path('contact/', ContactPView.as_view(), name='contact'),
]
