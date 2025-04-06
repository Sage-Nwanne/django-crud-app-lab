from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('parks/', views.parks_index, name='park-index'),
    path('parks/<int:park_id>/', views.parks_detail, name='park-detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='park-create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='park-update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='park-delete'),
    path('parks/<int:park_id>/add_attraction/', views.add_attraction, name='add-attraction'),
    path('attractions/<int:pk>/update/', views.AttractionUpdate.as_view(), name='attraction-update'),
    path('attractions/<int:pk>/delete/', views.AttractionDelete.as_view(), name='attraction-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
