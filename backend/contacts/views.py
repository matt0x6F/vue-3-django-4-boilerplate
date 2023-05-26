from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from contacts.serializers import ContactSerializer
from contacts.models import Contact


class ContactList(APIView):
    """
    List all contacts, or create a new contact.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactSerializer
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        contacts = Contact.objects.all()
        return Response(contacts)

class ContactDetail(APIView):
    """
    Retrieve, update or delete a contact instance.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        contact_details = ContactDetail.objects.all()
        return Response(contact_details)
