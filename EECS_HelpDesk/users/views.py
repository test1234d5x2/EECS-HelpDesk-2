from .models import User
from .serialisers import UserSerialiser, UserUpdateSerialiser, ChangePasswordSerialiser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsAdminOrOwner

 
# Create your views here.
class UserDetails(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerialiser
    queryset = User.objects.all()
    permission_classes = (IsAdminOrOwner,)
    

class UserList(ListCreateAPIView):
    serializer_class = UserSerialiser
    queryset = User.objects.all()
    permission_classes = (IsAdmin,)


class DeleteUser(DestroyAPIView):
    serializer_class = UserSerialiser
    queryset = User.objects.all()
    permission_classes = (IsAdmin,)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerialiser
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serialiser = self.get_serializer(data=request.data)
        if (serialiser.is_valid()):
            serialiser.save()

            return Response(
                {"message": "Password Changed Successfully."},
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"message": "Error changing password."}
        )