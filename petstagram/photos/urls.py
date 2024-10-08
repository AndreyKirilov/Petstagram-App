from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('add/', views.add_photo, name='add-page'),
    path('<int:pk>', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.edit_photo, name='edit-photo')
    ]))
]
