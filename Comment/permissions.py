from rest_framework.permissions import BasePermission;

from Project.models import Task
    
class IsBelongsToTask(BasePermission):
    def has_permission(self, request, view):
        
        task = Task.objects.filter(id=view.kwargs.get('pk'), members__id=request.user.id).first();

        if task is None:
            return False
        
        return False;


