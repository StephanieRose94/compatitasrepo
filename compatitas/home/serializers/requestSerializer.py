from django.db.models import fields
from home.models.petModel import PetModel
from home.models.managerModel import User,UserManager
from home.models.requestModel import RequestModel
from rest_framework import serializers

class RequestSerializer (serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = ['request_id', 'applicant_name','applicant_last_name','document_id','applicant_age','address','phone','email','income','activity','reason','request_status','pet_id','admin_id']

    