from rest_framework import serializers

class AktyorSerializer(serializers.Serializer):
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    tugilgan_sana = serializers.DateField()

class TarifSerializer(serializers.Serializer):
    nom = serializers.CharField()
    davomiylik = serializers.CharField()
    narx = serializers.IntegerField()
