from rest_framework import serializers
from reward.models import TestCard, User, Wallet


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = '__all__'


class TestCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCard
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
