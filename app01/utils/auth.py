from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01.models import UserToken

class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        token=request.META.get("HTTP_AUTHENTICATION")
        print("token",token)
        usertoken = UserToken.objects.filter(token=token).first()
        if usertoken:
            return usertoken.user,token
        else:
            raise AuthenticationFailed("auth failed!")

