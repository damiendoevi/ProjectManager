from rest_framework.permissions import BasePermission;

    
class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user and user.is_authenticated:
            return True
        
        return False