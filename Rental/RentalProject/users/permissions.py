from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allow read only if authenticated.
    Allow write only for admin users.
    """

    def has_permission(self, request, view):
        # Require authentication for all requests (including GET)
        if not request.user or not request.user.is_authenticated:
            return False

        # For read-only methods, allow any authenticated user
        if request.method in SAFE_METHODS:
            return True

        # For unsafe methods, only allow admin users
        return bool(request.user.is_superuser or getattr(request.user, 'role', None) == 'admin')