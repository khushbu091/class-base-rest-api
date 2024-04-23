from .models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        Employ = Employee.objects.all()
        serializer = EmployeeSerializer(Employ, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
