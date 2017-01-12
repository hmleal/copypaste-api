import json

from .models import Account
from .serializers import AccountSerializer

from django.http import Http404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AccountList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AccountDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AccountDelete(APIView):
    def get_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404

    def delete(self, request, *args, **kwargs):
        content = json.loads(request.body.decode('UTF-8'))
        account = self.get_object(content['email'])
        account.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
