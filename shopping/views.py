from rest_framework import viewsets, filters
from rest_framework.response import Response

from django.shortcuts import render
from django.db.models import Q
from .models import Category, Product
from .serializers import (
CategorySerializer,
ProductListSerializer,
ProductDetailSerializer,
)

# Create your views here.

def shopping(request):
    return render(request, 'shopping/shopping.html')

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related('category').prefetch_related('images', 'variants')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'brand']
    ordering_fields = ['price', 'created_at']
    lookup_field = 'slug'


def get_serializer_class(self):
    if self.action == 'retrieve':
        return ProductDetailSerializer
    return ProductListSerializer


def list(self, request, *args, **kwargs):
    qs = self.filter_queryset(self.get_queryset())


    category_slug = request.query_params.get('category')
    if category_slug:
        qs = qs.filter(category__slug=category_slug)


    q = request.query_params.get('q')
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(brand__icontains=q))


    ordering = request.query_params.get('ordering')
    if ordering in ['price', '-price', 'created_at', '-created_at']:
        qs = qs.order_by(ordering)


    page = self.paginate_queryset(qs)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
    return self.get_paginated_response(serializer.data)


    serializer = self.get_serializer(qs, many=True)
    return Response(serializer.data)