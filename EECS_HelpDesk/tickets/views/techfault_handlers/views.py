from ...models import TechFault
from ...serialisers import TechFaultReadSerialiser
from ...permissions import IsTechFaultHandler
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView


class TechFaultHandlerAssignedListView(ListAPIView):
    serializer_class = TechFaultReadSerialiser
    permission_classes = (IsTechFaultHandler, IsAuthenticated)

    def get_queryset(self):
        return TechFault.objects.filter(assigned_to=self.request.user)
    

class TechFaultHandlerTechFaultDetailsView(RetrieveAPIView):
    serializer_class = TechFaultReadSerialiser
    permission_classes = (IsTechFaultHandler, IsAuthenticated)
    queryset = TechFault.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']

        if not pk:
            return Response({
                "message": ""
            })
        
        obj = self.queryset.get(pk=pk)

        if obj.assigned_to != self.request.user:
            self.permission_denied(self.request, "You don't have permission to view this Technical Fault Ticket.")

        return obj