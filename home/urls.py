from django.urls import path

from . import views
from transactions.views import TransactionListView as transactions

urlpatterns = [
    path("", views.index, name="index"),
    path("sql-logs/", views.get_sql_logs, name="sql-logs"),
    path('transactions/', transactions.as_view(), name='transaction-list'),
]
