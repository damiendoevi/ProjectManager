from rest_framework.permissions import BasePermission;
from .models import Comment
    
class IsBelongsToTask(BasePermission):
    def has_permission(self, request, view):
        # Check if the comment is for the task of a project to which the user belongs
        comment = Comment.objects.filter(id=view.kwargs.get('pk'), task__members__id=request.user.id).first();

        if comment is None:
            return False
        
        return False;


