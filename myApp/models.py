from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


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
    medication = ArrayField(models.CharField(max_length=90, blank=True, null=False), size=6)
    date_of_recipe = models.DateField(verbose_name='Дата выдачи рецепта')
    medication.verbose_name = 'Препарат'
    medication.blank = True
    medication.null = True

    class Meta:
        verbose_name_plural = 'Льготники'

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.middle_name + ' ' + str(self.birth_date.year)


class Stats(models.Model):
    model_name = models.CharField(max_length=90, blank=False, null=True, verbose_name='Показатель')
    type_1 = models.IntegerField(default=0, verbose_name='Ветеран', editable=True)
    type_2 = models.IntegerField(default=0, verbose_name='Чернобыль', editable=False)
    type_3 = models.IntegerField(default=0, verbose_name='Ребёнок-инвалид до 18 лет', editable=False)
    type_4 = models.IntegerField(default=0, verbose_name='Инвалид I - II группы', editable=False)
    type_5 = models.IntegerField(default=0, verbose_name='Инвалид III группы', editable=False)

    class Meta:
        verbose_name_plural = 'Статистика'

    def __str__(self):
        return self.model_name


def stats_first():
    privileges = {'Ветеран': Stats.type_1, 'Чернобыль': Stats.type_2,
                  'Ребёнок-инвалид до 18 лет': Stats.type_3, 'Инвалид I - II группы': Stats.type_4,
                  'Инвалид III группы': Stats.type_5}

    q = Patient.objects.all()
    new_q = Stats.objects.filter(model_name='Первый показатель')
    for k, v in privileges.items():
        number = q.filter(privilege_type=k).count()
        new_q.update(type_2=1)

        # print(k + ' : ' + str(number))


stats_first()
