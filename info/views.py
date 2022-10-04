from rest_framework import generics
from rest_framework.views import APIView,Request,Response, status

from info.models import Info
from .serializers import InfoSerializer
from  django.shortcuts import get_object_or_404



class InfoViews(APIView):

    idadeAlunos = [12,13,30,15,16]
    altura_alunos = [1.70, 2.0, 1.40, 1.55, 1.70]
    
    media_altura = sum(altura_alunos) / float(len(altura_alunos))
    x = 0

    for j in range(len(idadeAlunos)):
        if idadeAlunos[j] >= 13:
            if altura_alunos[j] <= media_altura:
                x += 1

    print(x)

    lista = []

    with open('uploads/txt/CNAB','r') as result:
        for i in result:
            tipo = i[0]
            data = i[1:9]
            valor = int(i[9:19]) / 100
            cpf = i[19:30]
            cartao = i[30:42]
            hora = i[42:48]
            dono = i[48:62]
            store = i[62:81]

            dados = {
                'transaction':tipo,
                'date':data,
                'value': valor,
                'cpf':cpf,
                'card':cartao,
                'hour':hora,
                'owner':dono,
                'store':store
            }

            def post(self,request:Request) -> Response:
                

                serializer = InfoSerializer(data=self.dados)
                serializer.is_valid(raise_exception=True)
                
                serializer.save()
                
                return Response(serializer.data,status.HTTP_201_CREATED)

            def get(self,request: Request):
                info = Info.objects.all()
                serializer = InfoSerializer(info, many=True)
                return Response(serializer.data)