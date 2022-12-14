from rest_framework import serializers
from core.models import *

class wallets_serializer(serializers.ModelSerializer):
    class Meta:
        model = wallets
        fields = '__all__'

class wallets_types_serializer(serializers.ModelSerializer):
    class Meta:
        model = wallets_types
        fields = '__all__'

class wallets_balances_serializer(serializers.ModelSerializer):
    class Meta:
        model = wallets_balances
        fields = '__all__'

class transactions_types_serializer(serializers.ModelSerializer):
    class Meta:
        model = transactions_types
        fields = '__all__'

class transactions_serializer(serializers.ModelSerializer):
    class Meta:
        model = transactions
        fields = '__all__'

class revenue_items_serializer(serializers.ModelSerializer):
    class Meta:
        model = revenue_items
        fields = '__all__'

class cost_items_serializer(serializers.ModelSerializer):
    class Meta:
        model = cost_items
        fields = '__all__'