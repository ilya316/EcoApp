from rest_framework import serializers
import random

from .models import User

USER_NAMES_FIRST_PART = ["Useful", "Unexpected", "Curious", "Impossible", "Strong", "Beautiful", "Elegant"]
USER_NAMES_SECOND_PART = ["Bull", "Horse", "Cat", "Dog", "Mouse", "Chinchilla", "Hamster"]

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ( 'is_staff', 'is_superuser')
        
    def create(self, data):
        password = data.pop('password', None)
        try:
            data.pop('groups', None)
            data.pop('user_permissions', None)
        except:
            pass
        instance = self.Meta.model(**data)
        instance.is_active = True
        
        instance.name = random.choice(USER_NAMES_FIRST_PART) + " " + random.choice(USER_NAMES_SECOND_PART),
        instance.name = list(instance.name)[0]
        if password is not None:
            instance.set_password(password)

        instance.save()
  
        return instance 