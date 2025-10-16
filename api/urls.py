# api/urls.py
from django.urls import path
from .views import RegisterView, get_users, get_user, delete_user, expense_summary,home,CategoryCreateView,ExpenseCreateView

urlpatterns = [
    path('',home),
    path('register/', RegisterView.as_view()),
    path('users/', get_users),
    path('users/<int:pk>/', get_user),
    path('users/<int:pk>/delete/', delete_user),
    path('expenses/summary/', expense_summary),
    path('category/add/', CategoryCreateView.as_view()),
    path('expense/add/', ExpenseCreateView.as_view()),
]
