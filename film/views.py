from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
class HelloApi(APIView):
    def get(self, request):
        d = {
            "xabar": "Salom Dunyo",
            "qo'shimcha": "Bu-Api'imiz"
        }

        return Response(d)

    def post(self, request):
        data = request.data
        d = {
            "xabar":"Response 400",
            "response": data
        }
        return Response(d)


class MenHaqimda(APIView):
    def get(self, request):
        d = {
            "men": "Men Izzatullaev Abror, yoshim 22 da, Namangandanman, va katta bolaman",
        }

        return Response(d)

class AktyorlarApi(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor = request.data
        serializer = AktyorSerializer(data=aktyor)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            Aktyor.objects.create(
                ism = valid_data['ism'],
                tugilgan_sana=valid_data['tugilgan_sana'],
                jins = valid_data['jins'],
                davlat=valid_data['davlat']
            )
            return Response(valid_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AktyorApi(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

    def put(self, request, pk):
        data = request.data
        aktyor = Aktyor.objects.filter(id=pk)
        serializer = AktyorSerializer(aktyor, data=data)
        if serializer.is_valid():
            aktyor.update(
                davlat = serializer.validated_data.get("davlat")
            )

            return Response(serializer.data)
        return Response(serializer.errors)

class TarifApi(APIView):
    def get(self, request):
        tarif = Tarif.objects.all()
        serializer = TarifSerializer(tarif, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = TarifSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Tarif.objects.create(
                nom=validated_data['nom'],
                davomiylik=validated_data['davomiylik'],
                narx=validated_data['narx']
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TarifDeleteApi(APIView):
    def get(self, request,pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)
    def put(self, request, pk):
        tarif = Tarif.objects.filter(id=pk)
        data = request.data
        serializer = TarifSerializer(tarif, data=data)
        if serializer.is_valid():
            tarif.update(
                nom=serializer.validated_data['nom'],
                davomiylik = serializer.validated_data['davomiylik'],
                narx = serializer.validated_data['narx']
            )

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        Tarif.objects.get(id=pk).delete()
        return Response("muvaffaqiyatli o'chirildi")

class TarifUpdateApi(APIView):
    def get(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)

    def put(self, request, pk):
        tarif = Tarif.objects.filter(id=pk)
        data = request.data
        serializer = TarifSerializer(tarif, data=data)
        if serializer.is_valid():
            tarif.update(
                nom=serializer.validated_data['nom'],
                davomiylik = serializer.validated_data['davomiylik'],
                narx = serializer.validated_data['narx']
            )

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

