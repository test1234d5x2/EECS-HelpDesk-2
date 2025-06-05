from ...models import EC
from ...serialisers import ECReadSerialiser
from ...permissions import IsECHandler
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ECHandlerAssignedListView(ListAPIView):
    serializer_class = ECReadSerialiser
    permission_classes = (IsECHandler, IsAuthenticated)
    
    def get_queryset(self):
        return EC.objects.filter(assigned_to=self.request.user)


class ECHandlerECDetailsView(RetrieveAPIView):
    serializer_class = ECReadSerialiser
    permission_classes = (IsECHandler, IsAuthenticated)
    queryset = EC.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']

        if not pk:
            return Response({
                "message": ""
            })
        
        obj = self.queryset.get(pk=pk)

        if obj.assigned_to != self.request.user:
            self.permission_denied(self.request, "You don't have permission to view this EC.")

        return obj