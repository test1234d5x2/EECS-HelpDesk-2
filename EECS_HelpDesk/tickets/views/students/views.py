from ...models import EC, TechFault
from ...serialisers import ECReadSerialiser, ECCreateSerialiser, TechFaultReadSerialiser, TechFaultCreateSerialiser
from ...permissions import IsStudent
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView


class StudentCreateECView(CreateAPIView):
    serializer_class = ECCreateSerialiser
    permission_classes = (IsStudent, IsAuthenticated)


class StudentECListView(ListAPIView):
    serializer_class = ECReadSerialiser
    permission_classes = (IsStudent, IsAuthenticated)

    def get_queryset(self):
        return EC.objects.filter(student=self.request.user)


class StudentECDetailsView(RetrieveAPIView):
    serializer_class = ECReadSerialiser
    permission_classes = (IsStudent, IsAuthenticated)
    queryset = EC.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']

        if not pk:
            return Response({
                "message": ""
            })
        
        obj = self.queryset.get(pk=pk)

        if obj.student != self.request.user:
            self.permission_denied(self.request, "You don't have permission to view this EC.")

        return obj
    


class StudentCreateTechFaultView(CreateAPIView):
    serializer_class = TechFaultCreateSerialiser
    permission_classes = (IsStudent, IsAuthenticated)


class StudentTechFaultListView(RetrieveAPIView):
    serializer_class = TechFaultReadSerialiser
    permission_classes = (IsStudent, IsAuthenticated)

    def get_queryset(self):
        return TechFault.objects.filter(student=self.request.user)
    

class StudentTechFaultDetailsView(RetrieveAPIView):
    serializer_class = TechFaultReadSerialiser
    permission_classes = (IsStudent, IsAuthenticated)
    queryset = TechFault.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']

        if not pk:
            return Response({
                "message": ""
            })
        
        obj = self.queryset.get(pk=pk)

        if obj.student != self.request.user:
            self.permission_denied(self.request, "You don't have permission to view this Techincal Fault Ticket.")

        return obj
