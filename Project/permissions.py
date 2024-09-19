from rest_framework.permissions import BasePermission;
from .models import Project, Task
from django.db.models import Q
    
class IsProjectOwner(BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.filter(id=view.kwargs.get('pk'), admin__id=request.user.id).first();

        if project is None:
            return False
        
        return True;


class IsBelongsToProject(BasePermission):
    def has_permission(self, request, view):
        # Check if user is the owner or Belongs to project
        project = Project.objects.filter(Q(admin__id=request.user.id) | Q(members__id=request.user.id), id=view.kwargs.get('pk')).first();
        
        if project is None:
            return False
        
        return True;


class IsBelongsToTask(BasePermission):
    def has_permission(self, request, view):
        # Check if user is the owner or Belongs to project
        task = Task.objects.filter(Q(admin__id=request.user.id) | Q(members__id=request.user.id), id=view.kwargs.get('pk')).first();

        if task is None:
            return False
        
        return True;


class IsProjectOwnerThroughTask(BasePermission):
    def has_permission(self, request, view):
        # Check if user is the owner or Belongs to task project
        task = Task.objects.filter(Q(project__admin__id=request.user.id) | Q(project__members__id=request.user.id), id=view.kwargs.get('pk')).first();
        
        if task is None:
            return False
        
        return True;


class IsBelongsToTask(BasePermission):
    def has_permission(self, request, view):
        # Check if user is the owner or Belongs to project
        task = Task.objects.filter(Q(admin__id=request.user.id) | Q(members__id=request.user.id), id=view.kwargs.get('pk')).first();

        if task is None:
            return False
        
        return True;


class IsBelongsToProjectThroughTask(BasePermission):
    def has_permission(self, request, view):
        # Check if user is the owner or Belongs to project task
        task = Task.objects.filter(Q(project__admin__id=request.user.id) | Q(project__members__id=request.user.id), id=view.kwargs.get('pk')).first();

        if task is None:
            return False
        
        return True;

