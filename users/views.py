from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import MyTokenObtainPairSerializer


class TokenObtain(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
