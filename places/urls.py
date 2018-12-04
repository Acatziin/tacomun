from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('place/detail/<int:place_id>', views.detail_place, name = 'detail_place')
    # path('place/create/<int:place_id>', views.detail_place, name = 'create_place')
    # path('place/delete/<int:place_id>', views.detail_place, name = 'delete_place')
    # path('place/update/<int:place_id>', views.detail_place, name = 'update_place')
]
