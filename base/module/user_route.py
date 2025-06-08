from django.urls import path
from base.module.user_controller import (
    create_user,
    update_user,
    list_user,
    delete_user,
)

urlpatterns = [
    path("users/", list_user, name="list_user"),
    path("users/create/", create_user, name="create_user"),
    path("users/<int:user_id>/edit/", update_user, name="update_user"),
    path("users/<int:user_id>/delete/", delete_user, name="delete_user"),
]
