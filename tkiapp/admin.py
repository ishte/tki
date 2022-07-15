from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *

# Register your models here:

admin.site.site_header='The kreative ideas '
admin.site.index_title='Welcome to Superadmin Panel'



class RegistrationAdmin(BaseUserAdmin):
    add_form=customUserCreationForm
    form=customeUserChangeForms 
    model=Registration
    list_display=('id','username','password','mobile_no',)
#     fieldsets=(
#         ('permissions',{'fields':('username','email','mobile_no','password','is_active','is_staff','is_superuser','groups','user_permissions',)}),
 
#     )
admin.site.register(Registration,RegistrationAdmin)


# @admin.register(PaymentTracker)
# class PaymentTrackingAdmin(admin.ModelAdmin):
#     list_display=('total_paid','payment_mode','project_detail')
#     fields=('project_id','total_paid','payment_mode','project_detail')
    

@admin.register(PaymentInstallment)
class PaymentInstallmentAdmin(admin.ModelAdmin):
    list_display=('project_id','project_detail','total_project_value','booking_amount','total_paid','remaining_amountt','enter_amount')
    fields=('project_id','project_detail','total_project_value','booking_amount','total_paid','enter_amount')


@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display=('user','project_detail','booking_amount','total_project_value','remaining_amount')
    fields=('user','project_detail','booking_amount','total_project_value')
    





@admin.register(ProjectTracker)
class ProjectTrackerAdmin(admin.ModelAdmin):
    list_display=('project_id','client_meeting','planning','requirements','design_ui_ux','framework','approval','development',
                  'testing','release','handover')
    
    fields=('project_id','client_meeting','planning','requirements','design_ui_ux','framework','approval','development','testing','release','handover')
    
    
    
    
    

@admin.register(TeamName)
class TeamNameAdmin(admin.ModelAdmin):
    list_display=('id','designation','name','profile_image','email')




@admin.register(TeamAssign)
class TeamAssignAdmin(admin.ModelAdmin):
    list_display=('user','project')
