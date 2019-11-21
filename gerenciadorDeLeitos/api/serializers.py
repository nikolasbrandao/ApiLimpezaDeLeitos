from ..models import Leito
from rest_framework import serializers

class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = ('id', 'codigo', 'predio', 'ala', 'andar', 'status_limpeza')

        def update(self, instance, validated_data):
            instance.codigo = validated_data.get('codigo', instance.codigo)
            instance.predio = validated_data.get('predio', instance.predio)
            instance.ala = validated_data.get('ala', instance.ala)
            instance.andar = validated_data.get('andar', instance.andar)
            instance.status_limpeza = validated_data.get('status_limpeza', instance.status_limpeza)

            instance.save()
            return instance
