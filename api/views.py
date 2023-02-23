from .models import Waste
from .serializers import WasteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta


class WasteAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        #print("7 days before date", date.today()-timedelta(days=7))
        #print("7 days before date", Waste.objects.filter(added_date__gte=date.today()-timedelta(days=7)))
        
        waste = Waste.objects.filter(added_date__gte=date.today()-timedelta(days=7))
        serializer = WasteSerializer(waste, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        for e in Waste.objects.all():
            if e.location==request.data['location'] and e.added_date == date.today():
                return Response({'msg':'This location already exists'})
            
        serializer = WasteSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created successfully',
                             'status':'success', 'create':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)