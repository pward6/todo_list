from . import views

from django.urls import path, include


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:item_id>/", views.detail, name="detail"),
    path('new_task/', views.new_task, name='new_task'),
    path('/<int:item_id>/edit/', views.edit_task, name='edit_task'),
    path('delete_task/<int:item_id>/', views.delete_task, name='delete_task'),
]