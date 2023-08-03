from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

class Note(models.Model):
    note_title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    note_content = models.TextField()
    pdf_files = models.ManyToManyField('UploadedPdf', blank=True)

    def __str__(self):
        return self.note_title

class QuestionPaper(models.Model):
    paper_title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    paper_content = models.TextField()
    pdf_files = models.ManyToManyField('UploadedPdf', blank=True)

    def __str__(self):
        return self.paper_title

class Syllabus(models.Model):
    syllabus_title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    syllabus_content = models.TextField()
    pdf_files = models.ManyToManyField('UploadedPdf', blank=True)

    def __str__(self):
        return self.syllabus_title

class UploadedPdf(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
