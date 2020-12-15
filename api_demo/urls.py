from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.user_list, name="Index"),
    path('users/<int:pk>/', views.user_detail, name="Detail"),
    path('users/count/', views.user_count, name="Count")
]
