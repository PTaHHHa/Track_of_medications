from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.db.models.signals import post_save


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
    medication.verbose_name = 'Препараты'
    medication.blank = True
    medication.null = True

    class Meta:
        verbose_name = 'Льготника'
        verbose_name_plural = 'Льготники'

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.middle_name + ' ' + str(self.birth_date.year)


class Stats(models.Model):
    model_name = models.CharField(max_length=90, blank=False, null=True, verbose_name='Показатель')
    type_1 = models.IntegerField(default=0, verbose_name='Ветеран', editable=False)
    type_2 = models.IntegerField(default=0, verbose_name='Чернобыль', editable=True)
    type_3 = models.IntegerField(default=0, verbose_name='Ребёнок-инвалид до 18 лет', editable=False)
    type_4 = models.IntegerField(default=0, verbose_name='Инвалид I - II группы', editable=False)
    type_5 = models.IntegerField(default=0, verbose_name='Инвалид III группы', editable=False)

    class Meta:
        verbose_name_plural = 'Статистика'
        verbose_name = 'Статистику'

    def __str__(self):
        return self.model_name


def stats_first():
    privilege_list = ['Ветеран', 'Чернобыль', 'Ребёнок-инвалид до 18 лет', 'Инвалид I - II группы',
                      'Инвалид III группы']
    q = Patient.objects.all()
    number_1 = [q.filter(privilege_type=i).count() for i in privilege_list]
    type_list = ['type_1', 'type_2', 'type_3', 'type_4', 'type_5']

    field_name = Stats.objects.values_list('model_name')[1][0]
    new_q = Stats.objects.filter(model_name=field_name)[0]

    for i in range(len(number_1)):
        setattr(new_q, type_list[i], number_1[i])
        new_q.save()


def update_account_signal(sender, created, **kwargs):
    if not created:
        try:
            stats_first()
        except IndexError:
            pass


post_save.connect(update_account_signal, sender=Patient)
