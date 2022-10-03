from django.urls import path
from projectApis import views

urlpatterns = [
    path('projectApis/', views.project_list),
    path('projectApis/<int:pk>/', views.project_detail),
]