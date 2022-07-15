# from dataclasses import field
from .models import *
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    class Meta:
        model=Registration
        fields=['id','email','username','password','mobile_no']

    def create(self, validated_data):
        password=validated_data['password']
        obj=Registration.objects.create(
            username=validated_data['username'],
            mobile_no=validated_data['mobile_no'],
            email=validated_data['email'],
            password=password
        )
        obj.set_password(password)
        obj.save()
        return obj



class RegistrationSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=['fullname','location','gender','image','email','mobile_no']
                                
                                

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)




# class RegistrationSerializer1(serializers.ModelSerializer):
#     class Meta:
#         model=Registration
#         fields=['first_name','last_name','email']

        



class PaymentInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentInstallment
        fields='__all__'






class ProjecTrackeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectTracker
        fields='__all__'
        
        
    



class ProjectDeatailSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectDetail
        fields='__all__'







class TeamNameSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = TeamName
        fields = ("id","designation","name", "profile_image", "email")
        
    
class TeamAssignSerializer(serializers.ModelSerializer):
    team = TeamNameSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-id']
        model = TeamAssign
        fields = ("id", "user", "project", "team")
        extra_kwargs = {'team': {'required': False}}