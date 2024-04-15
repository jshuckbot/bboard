from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from api.serializers import BbDetailSerialiser, BbSerialiser, CommentSerialiser
from main.models import Bb, Comment


@api_view(["GET"])
def bbs(request):
    if request.method == "GET":
        bbs = Bb.objects.filter(is_active=True)[:10]
        serializer = BbSerialiser(bbs, many=True)
        return Response(serializer.data)


class BbDetailView(RetrieveAPIView):
    queryset = Bb.objects.filter(is_active=True)
    serializer_class = BbDetailSerialiser


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comments(request, pk):
    if request.method == "POST":
        serializer = CommentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        comments = Comment.objects.filter(is_active=True, bb=pk)
        serializer = CommentSerialiser(comments, many=True)
        return Response(serializer.data)
