from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notes(request):
    # Access query parameters: ?search=term
    search = request.query_params.get('search')
    
    notes = Note.objects.filter(owner=request.user)
    if search:
        notes = notes.filter(title__icontains=search)
    
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note(request):
    # Access JSON body or form input
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

