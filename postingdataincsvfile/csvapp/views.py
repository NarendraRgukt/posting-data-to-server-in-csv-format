from django.shortcuts import render
from rest_framework.views import APIView
from csvapp.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser,MultiPartParser
import csv

class CsvExportView(APIView):
    parser_classes=[FormParser,MultiPartParser]
    def post(self,request):
        try:
            csv_file=request.FILES.get('file')
            if not csv_file:
                return Response("there is no file in the request",status=status.HTTP_400_BAD_REQUEST)
            csv_data=[]
            csv_reader=csv.DictReader(csv_file)
            for row in csv_reader:
                csv_data.append(row)
            serializer=ItemSerializer(data=csv_data,many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("data loaded successfully",status=status.HTTP_201_CREATED)
        except csv.Error as e:
            return Response("Error duringcsv  loadind process",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response('error during the loading process',status=status.HTTP_500_INTERNAL_SERVER_ERROR)



