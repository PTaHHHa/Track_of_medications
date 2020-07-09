from django.db import models


# Create your models here.


class Patient(models.Model):
    Privilege_type = (
        ('Ветеран', 'Ветеран'),
        ('Чернобыль', 'Чернобыль'),
        ('Ребёнок-инвалид до 18 лет', 'Ребёнок-инвалид до 18 лет'),
        ('Инвалид I - II группы', 'Инвалид I - II группы'),
        ('Инвалид III группы', 'Инвалид III группы'),
    )

    first_name = models.CharField(max_length=90, blank=False, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=90, blank=False, null=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=90, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    privilege_type = models.CharField(max_length=90, choices=Privilege_type, default=0, verbose_name='Льгота')
    medication = models.CharField(max_length=90, verbose_name='Препарат')
    date_of_recipe = models.DateField(verbose_name='Дата выдачи рецепта')

    class Meta:
        verbose_name_plural = 'Льготники'

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ': ' + self.medication


class Stats(models.Model):
    type_1 = models.IntegerField(default=0, verbose_name='Ветеран', editable=False)
    type_2 = models.IntegerField(default=0, verbose_name='Чернобыль', editable=False)
    type_3 = models.IntegerField(default=0, verbose_name='Ребёнок-инвалид до 18 лет', editable=False)
    type_4 = models.IntegerField(default=0, verbose_name='Инвалид I - II группы', editable=False)
    type_5 = models.IntegerField(default=0, verbose_name='Инвалид III группы', editable=False)

    class Meta:
        verbose_name_plural = 'Статистика'

    def __str__(self):
        return 'Данные'

