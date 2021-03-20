from rest_framework import serializers
from .models import Diabetes


class DiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diabetes # this is the model that is being serialized
        fields = ('name', 'pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin',
       'bmi', 'diabetes_pedigree_function', 'age')