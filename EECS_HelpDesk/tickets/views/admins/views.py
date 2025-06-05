from ...permissions import IsAdmin
from ...models import EC, TechFault
from ...serialisers import ECReadSerialiser, TechFaultReadSerialiser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class AdminECListView(ListAPIView):
    serializer_class = ECReadSerialiser
    permission_classes = (IsAdmin, IsAuthenticated)
    queryset = EC.objects.all()
    

class AdminECDetailView(RetrieveAPIView):
    serializer_class = ECReadSerialiser
    permission_classes = (IsAdmin, IsAuthenticated)
    queryset = EC.objects.all()



class AdmiTechFaultListView(ListAPIView):
    serializer_class = TechFaultReadSerialiser
    permission_classes = (IsAdmin, IsAuthenticated)
    queryset = TechFault.objects.all()


class AdminTechFaultDetailsView(RetrieveAPIView):
    serializer_class = TechFaultReadSerialiser
    permission_classes = (IsAdmin, IsAuthenticated)
    queryset = TechFault.objects.all()