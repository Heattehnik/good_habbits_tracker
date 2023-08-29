from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.user == obj.user:
            return True
        return False


class IsPublic(BasePermission):
    """
    Пользователь может видеть список публичных привычек
    без возможности их как-то редактировать или удалять.
    """

    def has_object_permission(self, request, view, obj):
        if obj.is_public:
            return True
        elif not obj.is_public and obj.user != request.user:
            return False
        else:
            return True
