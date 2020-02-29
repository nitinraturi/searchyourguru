from rest_framework import views, viewsets, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from . import selectors as tution_selectors
from . import services as tution_services
from .serializers import *
from apps.users.serializers import *


class TutionViewSet(viewsets.ViewSet):
    queryset = tution_selectors.get_categories()
    renderer_classes = [renderers.JSONRenderer]

    @action(detail=False, methods=['post'], url_name="create_tution", url_path="create", permission_classes=[IsAuthenticated])
    def create_tution(self, request):
        serializer = TutionCreateSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(tutor=request.user)
        return Response({'status': 1}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="update_tution", url_path="update", permission_classes=[IsAuthenticated])
    def update_tution(self, request):
        data = request.data
        tution = tution_selectors.get_tution(data.get('id'))
        serializer = TutionUpdateSerializer(tution, data=request.data, context={
                                            'request': request, 'tution': tution})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'ok': 1}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_name="tution_list", url_path="list", permission_classes=[IsAuthenticated])
    def tution_list(self, request):
        serializer = TutionListSerializer(
            tution_selectors.get_tutions(request.user), many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="search", url_path="search")
    def search(self, request):
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = tution_selectors.filtered_tution_data(
            **serializer.validated_data)
        serializer = TutionListSerializer(data, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="suggested_cities", url_path="suggested-cities")
    def suggested_cities(self, request):
        serializer = CitySuggestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        queryset = tution_selectors.get_suggested_cities(
            serializer.validated_data.get('location_keyword'))
        zc_serializer = ZipCodeSerializer(queryset, many=True)
        return Response({'data': zc_serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name="suggested_subjects", url_path="suggested-subjects")
    def suggested_subjects(self, request):
        serializer = SubjectSuggestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        queryset = tution_selectors.get_suggested_subjects(
            serializer.validated_data.get('subject_keyword'))
        sc_serializer = CategorySerializer(queryset, many=True)
        return Response({'data': sc_serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_name='tution_request', url_path='tution-request', permission_classes=[IsAuthenticated])
    def tution_request(self, request):
        serializer = TutionRequestSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(student=request.user)
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_name='tution_applied', url_path='tution-applied', permission_classes=[IsAuthenticated])
    def tution_applied(self, request):
        queryset = tution_selectors.tution_applied_requests(request.user)
        serializer = TutionAppliedSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
