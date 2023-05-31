from rest_framework import viewsets

from .models import Book
from .permissions import IsAdminUserOrReadOnly
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)
