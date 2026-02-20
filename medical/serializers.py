from rest_framework import serializers
from .models import Patient, Consultation

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
        
    def to_representation(self, instance):
        # Default representation uses the ID for the patient field
        rep = super().to_representation(instance)
        # We override the patient field in the read representation to show basic info
        rep['patient'] = {
            'id': instance.patient.id,
            'full_name': instance.patient.full_name,
            'email': instance.patient.email
        }
        return rep
