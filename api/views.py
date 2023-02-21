from .models import Waste
from .serializers import WasteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class WasteAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        waste = Waste.objects.all()
        serializer = WasteSerializer(waste, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = WasteSerializer(data=request.data)
        for e in Waste.objects.all():
            if e.location == request.data['location']:
                return Response({'msg':'This location already exists'})
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created successfully',
                             'status':'success', 'create':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)