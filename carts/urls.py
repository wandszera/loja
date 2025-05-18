from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    # path('cart/', CartView.as_view(), name='cart'),
    # path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    # path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    # path('cart/update/<int:product_id>/', UpdateCartView.as_view(), name='update_cart'),
    # path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
    # path('cart/checkout/success/', CheckoutSuccessView.as_view(), name='checkout_success'),
    # path('cart/checkout/failure/', CheckoutFailureView.as_view(), name='checkout_failure'),
    # path('cart/checkout/payment/', PaymentView.as_view(), name='payment'),
]
