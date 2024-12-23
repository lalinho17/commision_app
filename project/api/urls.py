from django.urls import path
from fintech_app.views import UserListCreateView, AccountListCreateView, TransactionListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
]