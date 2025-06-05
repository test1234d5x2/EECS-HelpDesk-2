from django.urls import path
from .views import ModulesView, DeleteModuleView, CreateEnrollmentView, StudentEnrollmentDetailsView, AdminViewStudentEnrollmentsView

urlpatterns = [
    path("modules-list", ModulesView.as_view(), name='modules-list'),
    path("delete-module", DeleteModuleView.as_view(), name='delete-module'),
    path("enrol-student", CreateEnrollmentView.as_view(), name='enrol-student'),
    path("remove-enrolment", DeleteModuleView.as_view(), name="remove-enrolment"),
    path("my-enrolments", StudentEnrollmentDetailsView.as_view(), name="student-enrolments"),
    path("users/<int:user_pk>/enrolments", AdminViewStudentEnrollmentsView.as_view(), name="user-enrolments-list")
]