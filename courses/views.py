from django.shortcuts import render

# Create your views here.
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer
import logging

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.error(f"Error deleting course with ID {pk}: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# CourseInstance Views

class AddInstanceAPIView(APIView):
    def get(self, request):
        serializer = CourseInstanceSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstance
        fields = '__all__'  # or list specific fields like ['id', 'course', 'year', 'semester']
        
class AllInstancesView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer
    
    def get_queryset(self):
        return CourseInstance.objects.all()


class CourseInstanceListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year'] 
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)

class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer
    
    def delete(self, request, year, semester, course):
        try:
            instance = CourseInstance.objects.get(year=year, semester=semester, course_id=course)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CourseInstance.DoesNotExist:
            return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the error for debugging
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error deleting instance: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)
