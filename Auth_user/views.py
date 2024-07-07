from .models import *
from .serializer import *
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication





@api_view(['GET'])
def get_coreuser(request):
    obj = CoreUser.objects.all()
    ser = CoreUserSerializer(obj,many=True)
    return Response(ser.data)


class LoginView(APIView):
    def post(self,request):
        try:
            data = request.data 
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                print(f'Profile Name: {username}, Password: {password}')
                user = authenticate(username=username,password=password)
                print('\n\n\n')
                print(f'Authenticated User: {user}')
                if user is None:
                    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
                        
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                
                custom_claims = access_token.get('custom_claims', {})

                custom_claims['user_id'] = user.user_id
                custom_claims['first_name'] = user.first_name
                custom_claims['last_name'] = user.last_name
                access_token['custom_claims'] = custom_claims
                return Response({
                    'refresh': str(refresh),
                    'access': str(access_token),
                    'user': custom_claims
                }) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      
            
        except Exception as e:
            return Response({"message":str(e)}) 
 

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer