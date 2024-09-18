from rest_framework.permissions import BasePermission;
from .models import Project, Task
    
class IsProjectOwner(BasePermission):
    def has_permission(self, request, view):
        
        project = Project.objects.filter(id=view.kwargs.get('pk'), admin_id=request.user.id).first();

        if project is None:
            return False
        
        return False;

class IsBelongsToProject(BasePermission):
    def has_permission(self, request, view):
        
        project = Project.objects.filter(id=view.kwargs.get('pk'), members__id=request.user.id).first();

        if project is None:
            return False
        
        return False;


class IsBelongsToTask(BasePermission):
    def has_permission(self, request, view):
        
        task = Task.objects.filter(id=view.kwargs.get('pk'), members__id=request.user.id).first();

        if task is None:
            return False
        
        return False;


