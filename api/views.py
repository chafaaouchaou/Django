from django.shortcuts import render

from .models import Note
from .serialize import NoteSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.utils import timezone


# Create your views here.


@api_view(["GET"])
def  getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(["GET"])
def  get_notes(request):
    rooms = Note.objects.all()

    sirialised = NoteSerializer(rooms,many=True)

    return Response(sirialised.data)




@api_view(["GET"])
def  get_note(request,pk):
    notes = Note.objects.get(id=pk)

    sirialised = NoteSerializer(notes,many=False)

    return Response(sirialised.data)














@api_view(["POST"])
def  create_note(request):

    data = request.data

    print("\n\n\n")
    print(data)
    print("\n\n\n")

    note = Note.objects.create(
        body=data['body'],
        updated=timezone.now(),
        created=timezone.now()
    )
    sirialised = NoteSerializer(note,many=False)
    return Response(sirialised.data)



@api_view(["PUT"])
def  update_note(request,pk):

    data = request.data
    note = Note.objects.get(id=pk)
    
    sirialised = NoteSerializer( instance = note,data=data)
    if sirialised.is_valid():
        sirialised.save()
    
    sirialised.save()

    return Response(sirialised.data)
















@api_view(["DELETE"])
def  delete_note(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()


    return Response("note was deleted")