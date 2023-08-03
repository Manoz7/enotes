from rest_framework import generics
from apps.course.models import Course, Subject, Note, QuestionPaper, Syllabus, UploadedPdf
from ..serializer.course import CourseSerializer, SubjectSerializer, NoteSerializer, QuestionPaperSerializer, SyllabusSerializer, UploadedPdfSerializer


# Course views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Subject views
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Note views
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        pdf_files = self.request.FILES.getlist('pdf_files')
        note_instance = serializer.save()

        for pdf_file in pdf_files:
            uploaded_pdf = UploadedPdf.objects.create(
                title=pdf_file.name,
                course=note_instance.subject.course,
                pdf_file=pdf_file
            )
            note_instance.pdf_files.add(uploaded_pdf)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# QuestionPaper views
class QuestionPaperListCreateView(generics.ListCreateAPIView):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer

    def perform_create(self, serializer):
        pdf_files = self.request.FILES.getlist('pdf_files')
        question_paper_instance = serializer.save()

        for pdf_file in pdf_files:
            uploaded_pdf = UploadedPdf.objects.create(
                title=pdf_file.name,
                course=question_paper_instance.subject.course,
                pdf_file=pdf_file
            )
            question_paper_instance.pdf_files.add(uploaded_pdf)

class QuestionPaperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer

# Syllabus views
class SyllabusListCreateView(generics.ListCreateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

    def perform_create(self, serializer):
        pdf_files = self.request.FILES.getlist('pdf_files')
        syllabus_instance = serializer.save()

        for pdf_file in pdf_files:
            uploaded_pdf = UploadedPdf.objects.create(
                title=pdf_file.name,
                course=syllabus_instance.subject.course,
                pdf_file=pdf_file
            )
            syllabus_instance.pdf_files.add(uploaded_pdf)

class SyllabusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer


