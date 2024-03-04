from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Note

class NoteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Note.objects.create(title='Test Note', body='This is a test note.')

    def test_fetch_note_by_id(self):
        response = self.client.get(reverse('note-retrieve-update', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
