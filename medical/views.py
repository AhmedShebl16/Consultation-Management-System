from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Consultation
from .serializers import PatientSerializer, ConsultationSerializer
from .services import generate_medical_summary
from .serializers import PatientSerializer, ConsultationSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all().select_related('patient')
    serializer_class = ConsultationSerializer

    @action(detail=True, methods=['post'], url_path='generate-summary')
    def generate_summary(self, request, pk=None):
        consultation = self.get_object()

        if not consultation.symptoms:
            return Response(
                {'error': 'Cannot generate summary without symptoms.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            summary = generate_medical_summary(
                symptoms=consultation.symptoms,
                diagnosis=consultation.diagnosis or "Not provided"
            )
            
            consultation.ai_summary = summary
            consultation.save(update_fields=['ai_summary'])
            
            serializer = self.get_serializer(consultation)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to generate AI summary: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
