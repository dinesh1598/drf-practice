from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        
        return obj.owner == request.user
    # i can only have write permission because i am the ow



    
    
 # Read permissions are allowed to any request,
 # so we'll always allow GET, HEAD or OPTIONS requests
        