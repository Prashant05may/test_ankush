from django.urls import path
from new_app import views

urlpatterns = [
    path('mymodels/', views.mymodel_list),
    path('mymodels/<int:pk>/', views.mymodel_detail),
]