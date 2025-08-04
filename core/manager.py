from django.contrib.auth.base_user import BaseUserManager


class CustomuserManager(BaseUserManager):
     def create_user(self,email,password=None,**extra_fields):
          if not email:
               raise ValueError('Users Must have an email address')
          email=self.normalize_email(email)
          extra_fields.setdefault('is_active',True)
          user=self.model(email=email,**extra_fields)
          user.set_password(password)
          user.save(using=self._db)
          return user

     def create_superuser(self,email,password=None,**extra_fields):
         extra_fields.setdefault('is_staff',True)
         extra_fields.setdefault('is_superuser',True)
         if not password:
              raise ValueError("Superuser must have a  password ")
         return self.create_user(email,password,**extra_fields)
