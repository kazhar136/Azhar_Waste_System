from .models import Waste
from .serializers import WasteSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from datetime import date, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


# Register a new user and manually token generate..

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            user = User.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)

            
            return Response({'msg':'User created successfully',
                             'status':'success', 'create':serializer.data,'refresh': str(refresh),
                             'access': str(refresh.access_token)}, 
                             status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        


class WasteAPIView(APIView):
    serializer_class =  WasteSerializer
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self , request, format=None):
        #print("7 days before date", date.today()-timedelta(days=7))
        #print("7 days before date", Waste.objects.filter(added_date__gte=date.today()-timedelta(days=7)))
        
        waste = Waste.objects.filter(added_date__gte=date.today()-timedelta(days=7))
        serializer = self.serializer_class(waste, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        for e in Waste.objects.all():
            if e.location.lower()==request.data['location'].lower() and e.waste_type==request.data['waste_type'] and e.added_date == date.today():
                return Response({'msg':'This location already exists'})
                
          
        serializer = self.serializer_class(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created successfully',
                             'status':'success', 'create':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)