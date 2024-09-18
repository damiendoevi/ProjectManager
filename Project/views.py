from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwner, IsBelongsToTask, IsBelongsToProject
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.decorators import action


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.order_by('-id')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def join(self,request, pk=None):
        project = Project.objects.filter(code_invitation=request.data.get("code_invitation")).first();
        serializer = self.get_serializer(instance=project, data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        if user not in project.users.all():
            project.users.add(user);
            project.save()

        serializer = ProjectSerializer(project)

        return Response(serializer.data, status=status.HTTP_200_OK);


class TaskViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Task.objects.order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

