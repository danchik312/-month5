from django.urls import path
from users import views

urlpatterns = [
    path('registration/', views.RegisterAPIView.as_view(), name='register'),
    path('confirm/', views.ConfirmUserView.as_view(), name='confirm'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
]