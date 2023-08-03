from rest_framework import serializers
from apps.course.models import Course, Subject, Note, QuestionPaper, Syllabus, UploadedPdf

class UploadedPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedPdf
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    pdf_files = UploadedPdfSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = '__all__'

class QuestionPaperSerializer(serializers.ModelSerializer):
    pdf_files = UploadedPdfSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionPaper
        fields = '__all__'

class SyllabusSerializer(serializers.ModelSerializer):
    pdf_files = UploadedPdfSerializer(many=True, read_only=True)

    class Meta:
        model = Syllabus
        fields = '__all__'
