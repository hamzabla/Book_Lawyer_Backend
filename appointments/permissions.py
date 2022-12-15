from rest_framework import permissions

class IsLawyer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Lawyer_group').exists()


class IsAuthorOrNotView(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
