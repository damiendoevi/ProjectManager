from rest_framework import serializers
from .models import Project, Task
from Authentication.serializers import MyUserSerializer
from django.utils import timezone

class ProjectSerializer(serializers.ModelSerializer):
    members = MyUserSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = "__all__"


class InvitationCodeSerializer(serializers.Serializer):
    code_invitation = serializers.CharField()
    def validate(self, attrs):
        request = self.context.get('request')
        project_query = Project.objects.filter(code_invitation=attrs.get("code_invitation"));

        if (not project_query.first()):
            raise serializers.ValidationError({"detail": "Unable to join project with this code invitatioon"})

        if(project_query.filter(members__id=request.user.id).first()):
            raise serializers.ValidationError({"detail": "You've already joined this project"})
        
        return attrs


class TaskSerializer(serializers.ModelSerializer):
    members = MyUserSerializer(many=True, read_only=True)

    def validate(self, attrs):

        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if start_date > end_date:
            raise serializers.ValidationError(
                {"end_date": "The end date cannot be earlier than the start date."}
            )
        
        if self.instance is None and start_date < timezone.now():
            raise serializers.ValidationError(
                {"start_date": "The start cannot be earlier than the current date or now."}
            )
        
        return super().validate(attrs)

    class Meta:
        model = Task
        fields = "__all__"

    