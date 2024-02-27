from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class QuestionList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class QuestionDetail(generics.RetrieveAPIView):
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    


@api_view(['GET'])
def list_q(request):
    q=Question.objects.all()
    serializer = QuestionSerializer(q,many=True)
    questions = serializer.data
    return Response(questions)


@api_view(['GET'])
def list_detail(request, pk):
    try:
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    except Question.DoesNotExist:
        return Response({"error": "Question not found."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['PUT'])
def ques_upd(request, pk):
    q = get_object_or_404(Question,id=pk)
    question = request.data
    serializer = QuestionSerializer(instance=q, data=question)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class QuestionDelete(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer