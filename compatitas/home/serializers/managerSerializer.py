from rest_framework import serializers
from home.models.user import User
from home.models.account import Account
from home.serializers.accountSerializer import AccountSerializer

class ManagerSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)       
        return {
                    'id': user.id, 
                    'username': user.username,
                    'name': user.name,
                    'email': user.email                    
                }