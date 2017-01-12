import json

from .models import Account, Message
from .serializers import AccountSerializer, MessageSerializer

from django.http import Http404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AccountList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Account.objects.filter(is_active=True)
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # TODO da pra melhorar
        content = json.loads(request.body.decode('UTF-8'))

        account = self._get_object(content['email'])
        account.is_active = False
        account.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404


class AccountDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class MessageList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        origin = self._get_object(request.data['origin'])
        destination = self._get_object(request.data['destination'])

        request.data['origin'] = origin.pk
        request.data['destination'] = destination.pk

        return self.create(request, *args, **kwargs)

    def _get_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404


class MessageDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
