from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.get_page,name=('index')),
    path('about',views.get_page1,name=('about')),
    path('contact',views.get_page2,name=('contact')),
    path('signup', views.get_page3,name=('signup')),
    path('login', views.get_page4,name=('login')),
    path('customer',views.customer,name='customer'),
    path('customers',views.savecustomer,name='customer'),
    #path('addtocart',views.add_to_cart,name='addtocart'),
    path('edit/<str:pk>', views.edit_data, name='edit'),
    #path('update/<str:pk>', views.update_data, name='update'),
    #path('addtocarts/<str:pk>', views.show_data, name='add_to_cart'),
    path('delete/<int:id>', views.del_data, name='delete'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
    path('store', views.store, name='store'),
    
]
