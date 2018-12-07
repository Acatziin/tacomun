from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('place/detail/<int:place_id>', views.detail_place, name = 'detail_place'),
    path('place/create/', views.create_place, name = 'create_place'),
    path('place/edit/<int:place_id>', views.edit_place, name = 'edit_place'),
    path('place/delete/<int:place_id>', views.delete_place, name = 'delete_place'),
    path('place/detail/add_evaluation/<int:place_id>', views.add_evaluation, name = 'add_evaluation')
]
