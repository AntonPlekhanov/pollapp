from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from pollsapp.models import Poll, Choice # Добавьте импорт
from .models import Vote  #  Импортируем Vote из api/models.py

class PollListView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data) #  Отправляем данные в JSON-формате

    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PollDetailView(APIView):
    def get_object(self, pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data) #  Отправляем данные в JSON-формате

    def put(self, request, pk):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VoteListView(APIView):
    def get(self, request):
        votes = Vote.objects.all()  #  Теперь Vote импортирован из api/models.py
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data) #  Отправляем данные в JSON-формате

    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

