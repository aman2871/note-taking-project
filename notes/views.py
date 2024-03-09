# notes/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', None)
        if title_substring:
            return Note.objects.filter(title__icontains=title_substring)
        return super().get_queryset()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class NoteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
