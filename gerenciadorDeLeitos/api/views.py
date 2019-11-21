from rest_framework import status
from rest_framework.views import APIView
from ..models import Leito
from . import serializers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class LeitosListView(APIView):

    def get(self, request):
        leitos = Leito.objects.all()
        serializer = serializers.LeitoSerializer(leitos, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            leito = Leito.objects.get(codigo=pk)
        except Leito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        novo_status_leito = request.data
        serializer = serializers.LeitoSerializer(instance=leito, data=novo_status_leito, partial=True)
        if (serializer.is_valid()):
            leito_salvo = serializer.save()
            return Response({"sucesso": True})
        return Response({"erro": serializer.errors})



