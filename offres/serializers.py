from rest_framework import serializers
from .models import Offre, Condidature

class CondidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condidature
        fields = '__all__'

class OffreSerializer(serializers.ModelSerializer):
    condidatures = CondidatureSerializer(many=True, read_only=True)

    class Meta:
        model = Offre
        fields = '__all__'
            
        

       

class OffrePublicSrerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'