from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Lead


class LeadsAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Lead.objects.all()

    def get(self, request, format=None):
        """
        Returns a list of all leads by the current user.
        """
        return Response(self.queryset.filter(created_by=self.request.user))
