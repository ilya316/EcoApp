from django.contrib.auth.models import BaseUserManager
import random

USER_NAMES_FIRST_PART = ['Useful', 'Unexpected', 'Curious', 'Impossible', 'Strong', 'Beautiful', 'Elegant']
USER_NAMES_SECOND_PART = ['Bull', 'Horse', 'Cat', 'Dog', 'Mouse', 'Chinchilla', 'Hamster']

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(
            email = self.normalize_email(email),
            name = random.choice(USER_NAMES_FIRST_PART) + " " + random.choice(USER_NAMES_SECOND_PART),
            #password = password
        )
        
        user.set_password(password)
        
        user.save()
        
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = email,
            name = "Admin " + random.choice(USER_NAMES_SECOND_PART),
            password = password
        )
        
        user.is_staff = True
        user.is_superuser = True
        
        user.save()
        
        return user