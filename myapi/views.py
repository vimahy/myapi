from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import HeroSerializer
from .models import Hero

@api_view(['GET', 'POST'])
def get_post_hero(request):
    # get all puppies
    if request.method == 'GET':
        heros = Hero.objects.all()
        serializer = HeroSerializer(heros, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    elif request.method == 'POST':
        return Response({})

