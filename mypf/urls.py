from django.urls import path

from .views import home_view, detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:project>/', detail_view, name='detail'),

]
