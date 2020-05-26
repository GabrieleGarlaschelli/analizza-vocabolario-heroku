from django.core.serializers.python import Serializer


class TestoSerializer(Serializer):
    """QUESTA CLASSE CI SERVE PER SERIALIZZARE UN TESTO"""
    def end_object(self, obj):
        self._current['id'] = obj._get_pk_val()
        self.objects.append(self._current)
