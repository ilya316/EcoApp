from rest_framework import serializers

from .models import User

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
        print(data)
        instance = User.objects.create(**data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
  
        return instance 