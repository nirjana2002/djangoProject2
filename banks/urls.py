from django.urls import path
from . import views

urlpatterns = [
    path('create-bank/', views.create_bank, name='create-bank'),
    path('update-bank/<int:b_id>', views.update_bank, name='update-bank'),
    path('delete-bank/<int:b_id>', views.delete_bank, name='delete-bank'),
]
