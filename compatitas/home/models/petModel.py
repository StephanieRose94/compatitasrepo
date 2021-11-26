from django.db import models

class PetModel(models.Model):
    pet_id=models.BigAutoField(primary_key=True)
    pet_name=models.CharField('nombre',max_length=30, blank=False)
    pet_age=models.CharField("edad", max_length=20)
    pet_color=models.CharField("color",max_length=20)
    pet_type=models.CharField("tipo", max_length=20, blank=False)
    pet_size=models.CharField("tamaño",max_length=20)
    pet_image=models.CharField("imagen", max_length=100)
    pet_description=models.CharField("descripción",max_length=100)
    pet_status=models.CharField("estado",max_length=20, default="Pendiente")