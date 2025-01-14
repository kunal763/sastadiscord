from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
@api_view(['GET'])
def getRoute(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    room=Room.objects.all()
    serializer=RoomSerializer(room,many=True)
    print(serializer)
    return Response(serializer.data)