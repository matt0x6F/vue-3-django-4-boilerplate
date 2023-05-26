from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from companies.models import Company
from companies.serializers import CompanySerializer

class CompanyList(APIView):
    """
    List all companies, or create a new company.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CompanySerializer
    
    queryset = Company.objects.all()

    def get(self, request, format=None):
        """
        Returns a list of all leads by the current user.
        """
        return Response(self.queryset.filter())
