from django.urls import path
from .views import FAQsView

urlpatterns = [
    path("FAQs", FAQsView.as_view(), name='FAQs')
]