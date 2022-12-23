from django.urls import path
from . import views

urlpatterns = [
    path("get_wallets_types/", views.get_wallets_types),
    path("create_wallets_type/",views.create_wallets_type),
    path("delete_wallets_type/",views.delete_wallets_type),
    path("get_wallets/", views.get_wallets),
    path("create_wallet/", views.create_wallet),
    path("delete_wallet/",views.delete_wallet),
    path("get_wallets_balances/", views.get_wallets_balances),
    path("get_transactions_types/", views.get_transactions_types),
    path("create_transactions_type/", views.create_transactions_type),
    path("delete_transactions_type/",views.delete_transactions_type),
    path("get_transactions/", views.get_transactions),
    path("create_transaction/", views.create_transaction),
    path("delete_transaction/", views.delete_transaction),
    path("get_revenue_items/",views.get_revenue_items),
    path("create_revenue_item/",views.create_revenue_item),
    path("delete_revenue_item/",views.delete_revenue_item),
    path("get_cost_items/", views.get_cost_items),
    path("create_cost_item/", views.create_cost_item),
    path("delete_cost_item/", views.delete_cost_item)
]