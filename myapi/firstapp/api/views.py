from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
@api_view()
@permission_classes([AllowAny])
def firstfunction(request):
    return Response({'message' : "we recieved the get request"})