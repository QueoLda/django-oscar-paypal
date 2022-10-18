from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarDashboardConfig


class ExpressCheckoutDashboardApplication(OscarDashboardConfig):
    name = 'paypal.express_checkout.dashboard'
    label = 'express_checkout_dashboard'
    namespace = 'express_checkout_dashboard'
    verbose_name = _('Express Checkout Dashboard')

    default_permissions = ["is_staff"]

    def get_urls(self):
        from . import views

        urlpatterns = [
            url('transactions/', views.TransactionListView.as_view(),
                 name='paypal-transaction-list'),
            url(r'^transactions/(?P<pk>\d+)/', views.TransactionDetailView.as_view(),
                 name='paypal-transaction-detail'),
        ]
        return self.post_process_urls(urlpatterns)
