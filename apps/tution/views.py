from rest_framework import views, viewsets, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from . import selectors as tution_selectors
from .serializers import *


class TutionViewSet(viewsets.ViewSet):
    queryset = tution_selectors.get_categories()
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=False, methods=['get'], url_name="get_subjects", url_path="subjects")
    def subjects(self, request):
        data = tution_selectors.get_subjects()
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
