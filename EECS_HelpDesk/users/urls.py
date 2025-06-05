from django.urls import path
from .views import UserDetails, DeleteUser, ChangePasswordView, UserList

urlpatterns = [
    path("admin/users", UserList.as_view(), name="admin-user-list-create"),
    path("admin/users/<int:pk>", UserDetails.as_view(), name="admin-user-details-update"),
    path("admin/users/<int:pk>", DeleteUser.as_view(), name="admin-user-delete"),
    path("change-password", ChangePasswordView.as_view(), name="change-password")
    
]