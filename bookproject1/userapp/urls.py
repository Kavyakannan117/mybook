from django.urls import path
from .import views
urlpatterns = [
    path("",views.listBook,name='booklist'),
    path('details/<int:book_id>/',views.detailsBook,name="userdetails"),
    path('useraddtocart/<int:book_id>/',views.add_to_cart,name="add_to_cart"),
    path("viewcart/",views.view_cart,name="viewcart"),
    path('increase/<int:item_id>/',views.increase_quantity,name="increase_quantity"),
    path('decrease/<int:item_id>/',views.decrease_quantity,name="decrease_quantity"),
    path('removefromcart/<int:item_id>/',views.remove_from_cart,name="remove_cart"),
    path('create-checkout-session/',views.create_checkout_session,name='create-checkout-session'),
    path('searchuser/',views.SearchBook,name='usersearch'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel'),
]
