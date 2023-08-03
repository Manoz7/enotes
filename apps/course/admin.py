from django.contrib import admin
from .models import Course, Subject, Note, QuestionPaper, Syllabus

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Note)
admin.site.register(QuestionPaper)
admin.site.register(Syllabus)
