from django.contrib.auth.models import Permission
# from knox.models import AuthToken
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import random
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# from .sendmail import *
from django.core.cache import cache
# from django.core.cache import cache
# Create your views here




# Registration Api:
class RegistrationView(APIView):
                            
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            username = request.GET.get('username')
            if cache.get(username):
                print('data from cache')
                register = cache.get(username)
                return JsonResponse(register, safe=False)
            else:
                if username:
                    obj = Registration.objects.filter(
                        username=username).first()
                    if obj:
                        serializer = RegistrationSerializer(obj)
                        cache.set(serializer.data['username'], serializer.data)
                        return Response(data=serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response({'message': 'Username not found'}, status=status.HTTP_404_NOT_FOUND)
                        # token, _ = Token.objects.get_or_create(user=user)
                        # return Response({'token': token.key}, status=200)

        except Exception as e:
            print(e)
            return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)



# Post data:
    def post(self, request):
        
        try:
            data = request.data
            serializer = RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
                
                # user=Registration.objects.get(username=serializer.data['username'])
                # refresh = RefreshToken.for_user(user)
                # return Response({'status':200,'payload':serializer.data,'refresh':str(refresh),
                                #  'access': str(refresh.access_token),'message':'your data is saved'})
            else:
                return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)





# Updateall things:
    def patch(self, request):
        try:
            username = request.GET.get('username')
            print("username:",username)
            data = request.data
            print("data:",data)
            if username:
                obj = Registration.objects.filter(username=username).first()
                if obj:
                    serializer = RegistrationSerializer1(obj, data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(data=serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({'message': 'Username not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Username is empty please provide username'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)



# Login Api:
class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                register = Registration.objects.filter(
                    username=username).first()
                if register:
                    if username and password:
                        user = authenticate(
                            username=username, password=password)
                        if user:
                            # return JsonResponse(register,safe=False)
                            s = RegistrationSerializer(register)
                            # user=Registration.objects.get(username=serializer.data['username'],password=serializer.data['password'])
                            refresh = RefreshToken.for_user(user)
    
                            return Response({'status':200,'payload':serializer.data,'refresh':str(refresh),
                                 'access': str(refresh.access_token),'message':'Login Sucessfully'})
                            
                        else:                        
                            return Response({'message': 'Invalid username and password'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    else:
                        return Response({
                            'message': 'username and password required'
                        }, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)





# Logout Api:
class LogOutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'message': 'logout'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': 'something went to wrong'}, status=status.HTTP_400_BAD_REQUEST)







# Payment Tracker Api:
class PaymentInstallmentView(APIView):
     permission_classes = [IsAuthenticated]                   
     def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    obj=PaymentInstallment.objects.filter(user__username=username)
                    if obj is not None:
                        serializer=PaymentInstallmentSerializer(obj,many=True)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Username is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)



# ProjectTracker Views:
class ProjectTrackerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            username=request.GET.get('username')
            project_id=request.GET.get('project_id')
            obj=ProjectTracker.objects.filter(username__username=username)
            if obj:
                serializer=ProjecTrackeSerializer(obj,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            elif project_id:
                obj =ProjectTracker.objects.filter(project__id=project_id)
                serializer = ProjecTrackeSerializer(obj,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            
            else:
                    return Response(data='Username not found',status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(data='Something went wrong',status=status.HTTP_400_BAD_REQUEST)




# ProjectDetailView  View:
# class ProjectDetailView(APIView):
#     def get(self,request):
#         try:
#             username=request.GET.get('username')
#             # print('username:',username)
#             project_id=request.GET.get('project_id')
#             obj=ProjectDeatail.objects.filter(username__username=username)
#             if obj:
#                 # print("obj:",obj)
#                 serializer=ProjectDeatailSerializer(obj,many=True)
#                 return Response(data=serializer.data,status=status.HTTP_200_OK)
#             elif project_id:
#                 obj =ProjectDeatail.objects.filter(project__id=project_id)
#                 serializer = ProjectDeatailSerializer(obj,many=True)
#                 return Response(data=serializer.data,status=status.HTTP_200_OK)
            
#             else:
#                     return Response(data='Username not found',status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             print(e)
#             return Response(data='Something went wrong',status=status.HTTP_400_BAD_REQUEST)
        






# ProjectDetailsViews:
class ProjectDetailView(APIView):
     permission_classes = [IsAuthenticated]
     def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    obj=ProjectDetail.objects.filter(user__username=username)
                    if obj is not None:
                        serializer=ProjectDeatailSerializer(obj,many=True)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Username is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)



# Team Api:
class TeamNameView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):       
        try:
            username=request.GET.get('username')
            if username is not None:
                obj=TeamAssign.objects.filter(user__username=username)
                print(obj)
                if obj is not None:               
                    print('obj:',obj)
                    serializer=TeamAssignSerializer(obj,many=True,context={'request': request})
                    print('serializer:',serializer)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Username is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
