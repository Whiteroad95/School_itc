from django.db import models


class ClassGroup(models.Model):
    class_word = models.CharField(max_length=255)
    class_number = models.PositiveIntegerField()
    class_dir: Teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Students(models.Model):
    username = models.CharField(max_length=255)
    class_group: ClassGroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    parents_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    students_photo = models.ImageField(upload_to='products/images/', blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lessons(models.Model):
    lesson_name = models.CharField(max_length=255)
    teacher: Teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class School():
    director: Headmaster = models.ForeignKey(Headmaster, on_delete=models.CASCADE)
    senior_teachers: Headteacher = models.ForeignKey(Headteacher, on_delete=models.CASCADE)
    teachers: Teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    classes: ClassGroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    students: Students = models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher: Students = models.ForeignKey(Students, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
