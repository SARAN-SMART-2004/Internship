from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolios/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('portfolio/<int:pk>/add_stock/', views.add_stock, name='add_stock'),
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
    path('register/', views.register, name='register'),
]
