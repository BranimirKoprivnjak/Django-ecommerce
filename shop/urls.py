from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('filter/<category>/', views.FilteredMainPage.as_view(), name='filtered'),
    path('product/<slug>/', views.ItemDetail.as_view(), name='product'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', views.AddToCart.as_view(), name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.RemoveFromCart.as_view(), name='remove-from-cart')
]

#notes: <category>/ and order-summary/ are same things
#       django returns 404, shop/ <category>/ [name='filtered_main']
#       The current path, shop/order-summary/, matched the last one
