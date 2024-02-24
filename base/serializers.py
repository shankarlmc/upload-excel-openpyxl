from rest_framework import serializers
from .models import ImportedData


class ImportedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportedData
        fields = "__all__"


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
