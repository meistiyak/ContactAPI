from rest_framework import viewsets
from .models import Contact
from .Serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created')
    serializer_class = ContactSerializer