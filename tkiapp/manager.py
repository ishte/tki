from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create(self,password=None,**extra_fields):
        if password:
            self.set_password(password)
            self.save(using=self._db)
            return self
        else:
            raise ValueError('Email id is required')
    
    
    
    def create_superuser(self,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff is true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser is true') 
        return self.create(password,**extra_fields)