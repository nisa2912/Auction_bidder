from django.urls import path
from . import views



urlpatterns =[

    path('login/', views.loginPage, name="login"),
    path('', views.gallery, name="gallery"),
    path('post/<str:pk>/', views.post, name="post"),
]