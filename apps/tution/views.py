from rest_framework import views, viewsets, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from . import selectors as tution_selectors
from . import services as tution_services
from .serializers import *


class TutionViewSet(viewsets.ViewSet):
    queryset = tution_selectors.get_categories()
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=False, methods=['get'], url_name="get_subjects", url_path="subjects")
    def subjects(self, request):
        data = tution_selectors.get_category_groups()
        json_data = []
        for subject, categories in data:
            categories_data = CategoryRelationSerializer(
                categories, many=True).data
            if categories_data:
                json_data.append({
                    "subject": CategorySerializer(subject).data,
                    "categories": categories_data
                })

        return Response({'data': json_data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="search", url_path="search")
    def search(self, request):
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = tution_selectors.filtered_tution_data(
            **serializer.validated_data)
        return Response({'data': data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="connection_add", url_path="connection/add", permission_classes=[IsAuthenticated])
    def connection_add(self, request):
        request.data['student_id'] = request.user.id
        serializer = ConnectionAddSerializer(data=request.data)
        if serializer.is_valid():
            tution_request = tution_services.add_tution_connection(
                serializer.validated_data.get('tutor'), request.user)
            data = {'success': 1}
            status_code = status.HTTP_200_OK
        else:
            data = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data, status=status_code)

    @action(detail=False, methods=['get'], url_name="connection_list", url_path="connection/list", permission_classes=[IsAuthenticated])
    def connection_list(self, request):
        queryset = tution_selectors.get_connection_list(request.user)
        serializer = TutionRequestSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
