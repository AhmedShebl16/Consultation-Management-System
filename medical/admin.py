from django.contrib import admin
from .models import Patient, Consultation

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date_of_birth')
    search_fields = ('full_name', 'email')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'created_at')
    search_fields = ('patient__full_name', 'symptoms', 'diagnosis')
    list_filter = ('created_at',)
