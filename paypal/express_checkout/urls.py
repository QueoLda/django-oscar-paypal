from django.conf.urls import url

from paypal.express_checkout import views
from paypal.express_checkout.gateway import buyer_pays_on_paypal

base_patterns = [
    # Views for normal flow that starts on the basket page
    url('redirect/', views.PaypalRedirectView.as_view(), name='express-checkout-redirect'),
    url('cancel/<int:basket_id>/', views.CancelResponseView.as_view(),
         name='express-checkout-cancel-response'),
    # View for using PayPal as a payment method
    url('payment/', views.PaypalRedirectView.as_view(as_payment_method=True),
         name='express-checkout-direct-payment'),
]


buyer_pays_on_paypal_patterns = [
    url('handle-order/<int:basket_id>/',
         views.SuccessResponseView.as_view(preview=True),
         name='express-checkout-handle-order'),
]

buyer_pays_on_website_patterns = [
    url('place-order/<int:basket_id>/', views.SuccessResponseView.as_view(),
         name='express-checkout-place-order'),
    url('preview/<int:basket_id>/',
         views.SuccessResponseView.as_view(preview=True),
         name='express-checkout-success-response'),
]


if buyer_pays_on_paypal():
    urlpatterns = base_patterns + buyer_pays_on_paypal_patterns
else:
    urlpatterns = base_patterns + buyer_pays_on_website_patterns
