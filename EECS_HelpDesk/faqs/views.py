from rest_framework.generics import ListCreateAPIView
from .models import FAQs
from .permissions import IsNonStudent
from .serialisers import FAQSerialiser


class FAQsView(ListCreateAPIView):
    queryset = FAQs.objects.all()
    serializer_class = FAQSerialiser
    permission_classes = (IsNonStudent,)