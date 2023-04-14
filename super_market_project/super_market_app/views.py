from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AddSerializer
from .models import Add


class AddAPIView(APIView):
    def post(self, request):
        serializer = AddSerializer(data=request.data)
        if serializer.is_valid():
            value_1 = serializer.validated_data['value_1']
            value_2 = serializer.validated_data['value_2']
            result = value_1 + value_2
            add = Add.objects.create(value_1=value_1, value_2=value_2, result=result)
            add_serializer = AddSerializer(add)
            return Response(add_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
