from .serialisers import ModuleSerialiser, EnrollmentSerialiser
from .models import Module, Enrollment
from users.models import User
from .permissions import IsAdmin, IsStudent
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response



class ModulesView(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerialiser
    permission_classes = (IsAdmin,)


class DeleteModuleView(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerialiser
    permission_classes = (IsAdmin,)


class CreateEnrollmentView(CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerialiser
    permission_classes = (IsAdmin,)

class DeleteEnrollmentView(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerialiser
    permission_classes = (IsAdmin,)


class StudentEnrollmentDetailsView(ListAPIView):
    serializer_class = EnrollmentSerialiser
    permission_classes = (IsStudent, IsAuthenticated)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Response(Enrollment.objects.filter(user=self.request.user))
        
        return Response({
            "message": "You must be authenticated first."
        })
    

class AdminViewStudentEnrollmentsView(ListAPIView):
    serializer_class = EnrollmentSerialiser
    permission_classes = (IsAdmin,)

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")

        if not user_pk:
            return Response(Enrollment.objects.none())
        
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise Response({
            "message": "No user was found."
        })

        return Response(Enrollment.objects.filter(user=user))