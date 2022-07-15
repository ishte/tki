from django.db import models
from django.contrib.auth.models import AbstractUser
from .sendmails import *




#creating an id for registration
def customer_generate_id():
    try:
        id=Registration.objects.count()
        if id is not None:
            return f"TKI{2003+id}"
        else:
            return f"TKI{2003}"
    except Exception as e:
        print(e)


#Registration table:
class Registration(AbstractUser):
    first_name=models.CharField(max_length=60, null=True, blank=True) 
    last_name=models.CharField(max_length=60, null=True, blank=True) 
    fullname=models.CharField(max_length=60,null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    image=models.ImageField(upload_to='image',null=True,blank=True)
    id=models.CharField(max_length=10, default=customer_generate_id,primary_key=True,editable=False)
    mobile_no=models.CharField(max_length=13)
    otp=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.username +"--"+ self.id)

    

    class Meta:
        verbose_name_plural='user'





#creating a id for Project_Detail
def project_detail_id():
    try:
        id=ProjectDetail.objects.count()
        if id is not None:
            return f"TKI{1003+id}"
        else:
            return f"TKI{1003}"
    except Exception as e:
        print(e)
        
   
class ProjectDetail(models.Model):
    user=models.ForeignKey(Registration,related_name='project_detail',on_delete=models.CASCADE)
    project_id=models.CharField(max_length=10,default=project_detail_id,primary_key=True,editable=False,help_text="This is The Project Id")
    project_detail=models.CharField(max_length=100,help_text="Enter Type (like website /app)")
    booking_amount=models.DecimalField(default=0.0,max_digits=10,decimal_places=2,help_text="Enter Booking amount")
    total_project_value=models.DecimalField(default=0.0,max_digits=10,decimal_places=2,help_text="Enter Total Project Value (in ₹)") 
    project_booking_date=models.DateTimeField(null=True,blank=True)
    remaining_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text="Enter remaing amount")
    # new_payment=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    
    
    def __str__(self):
        return str(self.user.username + " --"+self.project_id)
    
    def remaining_amount(self):
        return (self.total_project_value)-(self.booking_amount)
    
    # class Meta:
    #     verbose_name_plural='total_project_value'






#creating an id for payment_tracker
# def payment_tracker_generate_id():
#     try:
#         id=PaymentTracker.objects.count()
#         print("count----",id)
#         if id is not None:
#             return f"TKI{1001+id}"
#         else:
#             return f"{1001}"

#     except Exception as e:
#         print(e)

# class PaymentTracker(models.Model):
#     project_id=models.ForeignKey(ProjectDetail,related_name='project_details',on_delete=models.CASCADE)
#     project_detail=models.ForeignKey(ProjectDetail,related_name='project',on_delete=models.CASCADE)
#     total_paid = models.DecimalField(max_digits=10,decimal_places=2,help_text="Enter Total Paid Amount (in ₹)")
#     payment_mode = models.CharField(max_length=100)
    
#     def __str__(self):
#         return str(self.project_id)

    # class Meta:
    #     verbose_name_plural='Payment Tracker'






class PaymentInstallment(models.Model):
    project_id=models.ForeignKey(ProjectDetail,related_name='pi',on_delete=models.CASCADE)
    project_detail=models.ForeignKey(ProjectDetail,related_name='pd',on_delete=models.CASCADE)
    total_project_value=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text="Enter remaing amount")
    booking_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text="Enter remaing amount")
    total_paid = models.DecimalField(max_digits=10, null=True ,blank=True,decimal_places=2,help_text="Enter Total Paid Amount (in ₹)")
    remaining_amountt=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text="Enter remaing amount")
    enter_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text="Enter remaing amount")

    def remaining_amountt(self):
        return self.total_project_value-self.booking_amount-self.total_paid-self.enter_amount

    # def total_amount_due(self):
    #     return self.total_project_value-self.total_paid






                                



# creating an id for project_tracker:
def project_tracker_generate_id():
    try:
        id=ProjectTracker.objects.count()
        if id is not None:
            return f"TKI{1003+id}"
        else:
            return f"TKI{1003}"
    except Exception as e:
        print(e)

     
#creating model for ProjectTracker:
class ProjectTracker(models.Model):
    #user=models.ForeignKey(Registration,related_name='project_tracker',on_delete=models.CASCADE,null=True,blank=True)
    project_id=models.ForeignKey(ProjectDetail,related_name='project_tacker',on_delete=models.CASCADE)
    client_meeting=models.CharField(max_length=250,blank=True,null=True)
    planning=models.CharField(max_length=250,blank=True,null=True)
    requirements=models.CharField(max_length=250,blank=True,null=True)
    design_ui_ux=models.CharField(max_length=250,blank=True,null=True)
    framework=models.CharField(max_length=250,blank=True,null=True)
    approval=models.CharField(max_length=250,blank=True,null=True)
    development=models.CharField(max_length=250,blank=True,null=True)
    testing=models.CharField(max_length=250,blank=True,null=True)
    release=models.CharField(max_length=250,blank=True,null=True)
    handover=models.CharField(max_length=250,blank=True,null=True)

    
    # def __str__(self):
    #     return self.user + " - " + self.project_id

    
    





   

#creating a id TeamName
def team_name_id():
    try:
        id=TeamName.objects.count()
        if id is not None:
            return f"TKI{1003+id}"
        else:
            return f"TKI{1003}"
    except Exception as e:
        print(e)
 

# TeamName Models:
class TeamName(models.Model):
    id=models.CharField(max_length=10,default=team_name_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=80,blank=True, null=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(upload_to='profile_image/',blank=True,null=True)
    email=models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return str (self.name + " - " + self.email)



# Team Assign Models:
class TeamAssign(models.Model):
    user=models.ForeignKey(Registration,related_name='Teama',on_delete=models.CASCADE,null=True, blank=True)
    project=models.ForeignKey(ProjectDetail,related_name='Teamsa',on_delete=models.CASCADE, null=True, blank=True)
    team= models.ManyToManyField(TeamName, related_name="team_lista",blank=True,)

    def __str__(self):
        return str (self.user.username)

    






