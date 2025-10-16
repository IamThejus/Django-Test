from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Category, Expense
from .serializers import RegisterSerializer, UserSerializer,CategorySerializer,ExpenseSerializer
from django.db.models import Sum

# Create your views here.

@api_view(["GET"])
def home(request):
    return Response({
        "message": "Welcome to the API!",
        "endpoints": {
            "Register": "/register/",
            "List Users": "/users/",
            "Get User": "/users/<id>/",
            "Delete User": "/users/<id>/delete/",
            "Expense Summary": "/expenses/summary/"
        }
    })

# Register endpoint
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create Expense
class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# Users endpoints
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"message": "User deleted"})
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

# Expense summary
@api_view(['GET'])
def expense_summary(request):
    summary = Expense.objects.values('category__name').annotate(total=Sum('amount'))
    result = {item['category__name']: item['total'] for item in summary}
    return Response(result)
