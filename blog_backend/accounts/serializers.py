from rest_framework import serializers
from accounts.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = ['id', 'nom', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            nom=validated_data['nom'],
        )
        return user

# Serializer pour afficher un utilisateur
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'nom', 'username']