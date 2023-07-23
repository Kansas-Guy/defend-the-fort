from rest_framework import serializers
from .models import Donor, Roster

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['id','donor_name', 'donor_email', 'donor_phone', 'donor_address',
                  'donor_address', 'donor_city', 'donor_state', 'donor_zip', 'donor_student', 'is_approved' ]

class RosterSerializer(serializers.ModelSerializer):
    donors = DonorSerializer(many=True, read_only=True)
    class Meta:
        model = Roster
        fields = ['student_name', 'team', 'donors']