from django.urls import path

from .views import home_view, detail_view, contact

urlpatterns = [
    path('', home_view, name='home'),
]
