from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


SEX_MALE = 'ML'
SEX_FEMALE = 'FM'
SEX_UNKNOWN = 'UK'
SEX_CHOICES = (
    (SEX_MALE, _('Male')),
    (SEX_FEMALE, _('Female')),
    (SEX_UNKNOWN, _('Unnown')),
)

class Teacher(models.Model):
    name = models.CharField(_('Name'), max_length=180)
    enable = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    name = models.CharField(_('Class name'), max_length=120)
    teacher = models.ForeignKey(Teacher, verbose_name=_('Teacher'), 
                                on_delete=models.CASCADE, limit_choices_to={
                                    'enable': True
                                })
    enable = models.BooleanField(_('Is Active'), default=True)

    class Meta:
        verbose_name = _('ClassRoom')
        verbose_name_plural = _('ClassRooms')

    def __str__(self):
        return "%s %s" % (
            self.name,
            self.teacher.name
        )

class City(models.Model):
    name = models.CharField(_('Name'), max_length=180)
    enable = models.BooleanField(_('Is Active'), default=True)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Citites')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(_('Name'), max_length=180)
    email = models.EmailField(_('Email'), max_length=180)
    age = models.IntegerField(_('Age'))
    dob = models.DateField(_('Date of Birth'))
    cob = models.ForeignKey(City, verbose_name=_('City of Birth'), 
                            on_delete=models.CASCADE, limit_choices_to={
                                'enable': True
                            })
    classroom = models.ForeignKey(ClassRoom, verbose_name=_('ClassRoom'), 
                            on_delete=models.CASCADE, limit_choices_to={
                                'enable': True
                            })
    sex = models.CharField(_('Sex'), max_length=2, choices=SEX_CHOICES, default=SEX_UNKNOWN)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    
    def __str__(self):
        return "%s %s" % (
            self.classroom.name,
            self.name
        )
