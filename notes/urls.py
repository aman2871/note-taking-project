from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:id>/', NoteRetrieveUpdateView.as_view(), name='note-retrieve-update'),
]
