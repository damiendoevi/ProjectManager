from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwner, IsBelongsToTask, IsBelongsToProject, IsProjectOwnerThroughTask, IsBelongsToProjectThroughTask
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from Comment.serializers import CommentSerializer
from rest_framework.decorators import action
from django.db.models import Q


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.order_by('-id')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsBelongsToProject]

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

    @action(methods=["GET", "POST"], detail=True)
    def tasks(self, request, pk=None):
        if request.method == 'GET':
            project = self.get_object()

            tasks = project.tasks.order_by('-id')
            serializer = TaskSerializer(tasks, many=True)
        
            search_term = self.request.query_params.get('taskSearchInput', None)

            if search_term is not None:
                filtered_tasks = tasks.filter(Q(priority__icontains=search_term) | Q(status__icontains=search_term) | Q(title__icontains=search_term)| Q(description__icontains=search_term) | Q(members__first_name__icontains=search_term) | Q(members__last_name__icontains=search_term))
                serializer = TaskSerializer(filtered_tasks, many=True)

            return Response(serializer.data)
        
        elif request.method == 'POST':
            project = self.get_object()

            data_copy = request.data.copy()
            data_copy["project"] = project.id
            
            serializer = TaskSerializer(data=data_copy)
            serializer.is_valid(raise_exception=True)
            serializer.save(project=project)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_permissions(self):        
        if self.action == 'tasks' and self.request.method == 'POST' or self.action == 'update' or self.action == 'delete':
            self.permission_classes = [IsAuthenticated, IsProjectOwner]

        return super().get_permissions()



class TaskViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = Task.objects.order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsBelongsToProjectThroughTask]

    @action(methods=["GET", "POST"], detail=True)
    def comments(self, request, pk=None):
        if request.method == 'GET':
            task = self.get_object()

            comments = task.comments.all()
            serializer = TaskSerializer(comments, many=True)
        
            return Response(serializer.data)
        
        elif request.method == 'POST':
            task = self.get_object()

            data_copy = request.data.copy()
            data_copy["task"] = task.id
            
            serializer = CommentSerializer(data=data_copy)
            serializer.is_valid(raise_exception=True)
            serializer.save(task=task)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def get_permissions(self):        
        if self.action == 'delete':
            self.permission_classes = [IsAuthenticated, IsProjectOwnerThroughTask]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsBelongsToTask]

        return super().get_permissions()

