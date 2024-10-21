from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from global_functions import generate_exception
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class CategoryAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id=None):
        try:
            with transaction.atomic():
                if category_id:
                    category_instance = get_object_or_404(Category, id=category_id)
                    serializer = CategorySerializer(category_instance)
                    return Response({'success': True, 'details': serializer.data}, status=status.HTTP_200_OK)
                
                categories = Category.objects.order_by('-id')
                serializer = CategorySerializer(categories, many=True)
                return Response({'success': True, 'details': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            with transaction.atomic():
                serializer = CategorySerializer(data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response({'success': True, 'details': serializer.data}, status=status.HTTP_201_CREATED)
                generate_exception(serializer.errors)
                return Response({'success': False, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, category_id=None):
        try:
            with transaction.atomic():
                category_instance = get_object_or_404(Category, id=category_id)
                serializer = CategorySerializer(category_instance, data=request.data, context={'request': request}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"success": True, 'details': serializer.data}, status=status.HTTP_200_OK)
                generate_exception(serializer.errors)
                return Response({"success": False, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id=None):
        try:
            with transaction.atomic():
                category_instance = get_object_or_404(Category, id=category_id)
                category_instance.delete()
                return Response({"success": True, 'details': "Deleted Successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, product_id=None):
        try:
            with transaction.atomic():
                # import pdb;pdb.set_trace()
                category_id = request.GET.get("category", None) or None
                if product_id:
                    if category_id:
                        product_instance = get_object_or_404(Product, id=product_id, category_id=category_id)
                    else:
                        product_instance = get_object_or_404(Product, id=product_id)
                    serializer = ProductSerializer(product_instance)
                    return Response({'success': True, 'details': serializer.data}, status=status.HTTP_200_OK)

                if category_id:
                    products = Product.objects.filter(category_id=category_id).order_by('-id')
                else:
                    products = Product.objects.order_by('-id')

                page_count = int(request.GET.get('count', 2))
                page_no = int(request.GET.get('page', 1))

                paginator = Paginator(products, page_count)

                try:
                    data = paginator.page(page_no)
                except PageNotAnInteger:
                    return Response({'success': False, 'details': "Invalid page number."}, status=status.HTTP_400_BAD_REQUEST)
                except EmptyPage:
                    return Response({'success': False, 'details': "No more products available."}, status=status.HTTP_404_NOT_FOUND)

                serializer = ProductSerializer(data.object_list, many=True)

                return Response({
                    'success': True,
                    'details': serializer.data,
                    'pagination': {
                        'current_page': page_no,
                        'total_pages': paginator.num_pages,
                        'total_products': paginator.count
                    }
                }, status=status.HTTP_200_OK)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            with transaction.atomic():
                serializer = ProductSerializer(data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response({'success': True, 'details': serializer.data}, status=status.HTTP_201_CREATED)
                generate_exception(serializer.errors)
                return Response({'success': False, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id=None):
        try:
            with transaction.atomic():
                # import pdb;pdb.set_trace()
                product_instance = get_object_or_404(Product, id=product_id)
                serializer = ProductSerializer(product_instance, data=request.data, context={'request': request}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'success': True, 'details': serializer.data}, status=status.HTTP_200_OK)
                generate_exception(serializer.errors)
                return Response({'success': False, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id=None):
        try:
            with transaction.atomic():
                product_instance = get_object_or_404(Product, id=product_id)
                product_instance.delete()
                return Response({'success': True, 'details': "Deleted Successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            generate_exception(e)
            return Response({'success': False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)
