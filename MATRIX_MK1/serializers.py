from .models import *


class DatatableSerializer(Datatable.ModelSerializer):
    class Meta:
        model = Datatable
        fields = '__all__'
