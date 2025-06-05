from rest_framework import serializers
from users.serialisers import UserSerialiser
from modules.serialisers import ModuleSerialiser
from modules.models import Module
from .models import EC, ECFileUploads, TechFault, TechFaultFileUploads
import uuid


class ECFileUploadsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ECFileUploads
        fields = '__all__'
        read_only_fields = ('ticket', 'uploaded_at',)


class ECReadSerialiser(serializers.ModelSerializer):
    student = UserSerialiser(read_only=True) 
    assigned_to = UserSerialiser(read_only=True) 
    module_code = ModuleSerialiser(read_only=True)

    files = ECFileUploadsSerialiser(many=True, read_only=True)

    class Meta:
        model = EC
        fields = '__all__'
        read_only_fields = ('id', 'student', 'date_submitted', 'assigned_to', 'status')


class ECCreateSerialiser(serializers.ModelSerializer):
    module_code = serializers.SlugRelatedField(
        slug_field='code',
        queryset=Module.objects.all(),
        write_only=True,
        help_text="The code of the module this EC applies to (e.g., 'ECS101A')."
    )

    class Meta:
        model = EC
        fields = (
            'nature_of_circumstance',
            'further_explanation',
            'module_code', 
            'assessment_type',
            'assessment_submission_date',
            'requested_outcome',
            'requested_extended_deadline_date',
        )

        read_only_fields = (
            'id',
            'student',
            'date_submitted',
            'assigned_to', 
            'status',
        )

    def create(self, validated_data):
        """
        Overrides the create method to set the 'id' field automatically.
        The 'student' and 'assigned_to' fields will be handled in the view.
        """
        if 'id' not in validated_data:
            validated_data['id'] = str(uuid.uuid4())
        return super().create(validated_data)



class TechFaultFileUploadsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = TechFaultFileUploads
        fields = '__all__'
        read_only_fields = ('ticket', 'uploaded_at',)


class TechFaultReadSerialiser(serializers.ModelSerializer):
    student = UserSerialiser(read_only=True) 
    assigned_to = UserSerialiser(read_only=True) 

    files = TechFaultFileUploadsSerialiser(many=True, read_only=True)

    class Meta:
        model = TechFault
        fields = '__all__'
        read_only_fields = ('id', 'student', 'date_submitted', 'assigned_to', 'status')


class TechFaultCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = TechFault
        fields = ("explanation", "location")

        read_only_fields = (
            'id',
            'student',
            'date_submitted',
            'assigned_to', 
            'status',
        )

    def create(self, validated_data):
        """
        Overrides the create method to set the 'id' field automatically.
        The 'student' and 'assigned_to' fields will be handled in the view.
        """
        if 'id' not in validated_data:
            validated_data['id'] = str(uuid.uuid4())
        return super().create(validated_data)
