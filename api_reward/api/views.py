from rest_framework import viewsets

from reward.models import TestCard, User, Wallet
from .serializers import TestCardSerializer, WalletSerializer, UserSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestCardViewSet(viewsets.ModelViewSet):
    queryset = TestCard.objects.all()
    serializer_class = TestCardSerializer
