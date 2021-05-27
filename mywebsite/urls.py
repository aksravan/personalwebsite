from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('project/<int:id>/', views.projectview, name='product_detail')
]