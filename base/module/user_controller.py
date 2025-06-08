from django.shortcuts import render, redirect
from base.module.user_service import (
    create_user_service,
    update_user_service,
    list_users_service,
    delete_user_service,
)
from base.models import User

def create_user(request):
    if request.method == "POST":
        data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "is_active": bool(request.POST.get("is_active")),
        }
        create_user_service(data)
        return redirect("list_user")
    return render(request, "user_form.html")

def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "is_active": bool(request.POST.get("is_active")),
        }
        update_user_service(user_id, data)
        return redirect("list_user")
    return render(request, "user_form.html", {"user": user})

def list_user(request):
    users = list_users_service()
    return render(request, "user_list.html", {"users": users})

def delete_user(request, user_id):
    delete_user_service(user_id)
    return redirect("list_user")
