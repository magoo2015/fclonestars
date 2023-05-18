from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def players_list(request):

    return Response('ok')
