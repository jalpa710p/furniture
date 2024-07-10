from django.urls import path
from .import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),  # Keeping this if you want 'index/' URL too
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('editcart/<int:id>/', views.editcart, name='editcart'),
    path('deletecart/<int:id>/', views.deletecart, name='deletecart'),
    path('addcart/', views.addcart, name='addcart'),

]
