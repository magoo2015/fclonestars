from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FcplayersSerializer
from .models import Fcplayers

@api_view(['GET', 'POST'])
def players_list(request):

    if request.method == 'GET':
        players = Fcplayers.objects.all()
        serializer = FcplayersSerializer(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
            serializer = FcplayersSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    

    