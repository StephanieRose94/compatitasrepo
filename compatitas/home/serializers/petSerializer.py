from django.db.models import fields
from home.models.petModel import PetModel
from rest_framework import serializers

class PetSerializer (serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = ['pet_id','pet_name','pet_age','pet_color','pet_type','pet_size','pet_image','pet_description','pet_status']

