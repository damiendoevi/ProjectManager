from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsBelongsToTask


class CommentViewSet(mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsBelongsToTask]