# from routerproj.routerapp.models import Router
from django.db import router
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .Serializers import RouterSerializer
from .models import Router
from rest_framework import filters
import ipaddress 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views he


class RouterCreateAPIView(generics.CreateAPIView):
    queryset=Router.objects.all()
    serializer_class=RouterSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]


class RouterAPIView(generics.ListAPIView):
    serializer_class=RouterSerializer
    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        qs=Router.objects.order_by('hostname')
        print(qs) 
        id1=self.request.GET.get('sapid')
        print(id1)
        if id1 is not None:
            qs=qs.filter(Router__icontains=id1)
        

        return qs
class RouterDetailAPIView(generics.RetrieveAPIView):
    search_fields = ['loopbackipv4']
    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    queryset=Router.objects.all()
    serializer_class=RouterSerializer
    lookup_field='sapid'
class RouterUpdateAPIView(generics.UpdateAPIView):
    search_fields = ['hostname']
    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    queryset=Router.objects.all()
    serializer_class=RouterSerializer
    lookup_field='loopbackipv4'

class RouterDeleteAPIView(generics.DestroyAPIView):
    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    queryset=Router.objects.all()
    serializer_class=RouterSerializer
    lookup_field='loopbackipv4'


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# import json
# from django.core.exceptions import ObjectDoesNotExist



# @api_view(["GET"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def welcome(request):
#     content = {"message": "Welcome to the Routers Data!"}
#     return JsonResponse(content)  


# @api_view(["GET"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def get_routers(request):
#     user = request.user.id
#     routers = Router.objects.filter(added_by=user)
#     serializer = RouterSerializer(routers, many=True)
#     return JsonResponse({'routers': serializer.data}, safe=False, status=status.HTTP_200_OK)

# # @api_view(["POST"])
# # @csrf_exempt
# # @permission_classes([IsAuthenticated])
# # def add_router(request):
# #     payload = json.loads(request.body)
# #     user = request.user
# #     try:
# #          = Router.objects.get(id=payload["author"])
# #         book = Router.objects.create(
# #             title=payload["title"],
# #             description=payload["description"],
# #             added_by=user,
# #             author=author
# #         )
# #         serializer = BookSerializer(book)
# #         return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
# #     except ObjectDoesNotExist as e:
# #         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
# #     except Exception:
# #         return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(["PUT"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def update_router(request, loopbackipv4):
#     print(type(loopbackipv4))
#     user = request.user.id
#     payload = json.loads(request.body)
#     try:
#         router_item = Router.objects.filter(loopbackipv4=loopbackipv4)
#         # returns 1 or 0
#         router_item.update(**payload)
#         router = Router.objects.get(loopbackipv4=loopbackipv4)
#         serializer = RouterSerializer(router)
#         return JsonResponse({'router': serializer.data}, safe=False, status=status.HTTP_200_OK)
#     except ObjectDoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     except Exception:
#         return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




