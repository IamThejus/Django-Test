import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def register_user(username, email, password):
    url = f"{BASE_URL}/register/"
    payload = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=payload)
    return response.json()


def get_all_users():
    url = f"{BASE_URL}/users/"
    response = requests.get(url)
    return response.json()


def get_user_by_id(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)
    return response.json()


def delete_user(user_id):
    url = f"{BASE_URL}/users/{user_id}/delete/"
    response = requests.delete(url)
    return response.status_code, response.text



def add_category(name):
    url = f"{BASE_URL}/category/add/"
    payload = {"name": name}
    response = requests.post(url, json=payload)
    return response.json()


def add_expense(title, category, amount, date):
    url = f"{BASE_URL}/expense/add/"
    payload = {
        "title": title,
        "category": category,   
        "amount": amount,
        "date": date
    }
    response = requests.post(url, json=payload)
    return response.json()

def get_expense_summary():
    url = f"{BASE_URL}/expenses/summary/"
    response = requests.get(url)
    return response.json()
