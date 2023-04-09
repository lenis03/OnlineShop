from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductsListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

]
