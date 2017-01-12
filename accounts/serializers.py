from rest_framework import serializers

from .models import Account, Message


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('email',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('origin','destination', 'content')
