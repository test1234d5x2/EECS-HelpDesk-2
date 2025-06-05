from django.urls import path
from .views import students, admins, ec_handlers, techfault_handlers

urlpatterns = [
    # Student URL paths
    path("ec-tickets/submit", students.StudentCreateECView.as_view(), name="submit-ec"),
    path("ec-tickets/my", students.StudentECListView.as_view(), name="student-ec-tickets"),
    path("ec-tickets/my/<str:pk>", students.StudentECDetailsView.as_view(), name="student-ec-details"),
    path("techfault-tickets/submit", students.StudentCreateTechFaultView.as_view(), name="submit-techfault"),
    path("techfault-tickets/my", students.StudentTechFaultListView.as_view(), name="student-techfault-tickets"),
    path("techfault-tickets/my/<str:pk>", students.StudentTechFaultDetailsView.as_view(), name="student-techfault-details"),

    # Admin URL paths
    path("ec-tickets/admin", admins.AdminECListView.as_view(), name="admin-ec-list"),
    path("ec-tickets/admin/<str:pk>", admins.AdminECDetailView.as_view(), name="admin-ec-details"),
    path("techfault-tickets/admin", admins.AdmiTechFaultListView.as_view(), name="admin-techfault-list"),
    path("techfault-tickets/admin", admins.AdminTechFaultDetailsView.as_view(), name="admin-techfault-details"),

    # EC Handlers URL paths
    path("ec-tickets/assigned", ec_handlers.ECHandlerAssignedListView.as_view(), name="ec-handlers-assigned-list"),
    path("ec-tickets/assigned/<str:pk>", ec_handlers.ECHandlerECDetailsView.as_view(), name="ec-handlers-assigned-details"),


    # Tech Fault Handlers URL paths
    path("techfault-tickets/assigned", techfault_handlers.TechFaultHandlerAssignedListView.as_view(), name="techfault-handlers-assigned-list"),
    path("techfault-tickets/assigned/<str:pk>", techfault_handlers.TechFaultHandlerTechFaultDetailsView.as_view(), name="techfault-handlers-assigned-details"),
]