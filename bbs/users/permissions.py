from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #request가 본 메소드가 퍼미션에서 안전하다고 판단하는 메소들 중에 우리가 찾고 있는 메소드가 있다면
            return True
        return obj.auther == request.user #안전하지 않을 경우, 사용자와 소유권자가 같을 경우에만 사용하겠다.
