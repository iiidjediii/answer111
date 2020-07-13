from django.db import models
import datetime

class Vote(models.Model):
    vote_title = models.CharField('Название голосования', max_length=100)
    start_date = models.DateTimeField('Дата начала голосования')
    end_date = models.DateTimeField('Дата конца голосования')
    limit_of_votes = models.IntegerField('Количество голосов для завершения', default=10)
    #status_vote = models.BooleanField('статус голосования')

    def __str__(self):
        return self.vote_title

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'


class Person(models.Model):

    vote_id = models.ForeignKey(Vote, on_delete=models.CASCADE)
    votes = models.IntegerField('Голосов', default=0)
    person_name = models.CharField('Имя', max_length=50)
    person_surname = models.CharField('Фамилия', max_length=50)
    person_patronymic = models.CharField('Отчество', max_length=50)
    person_photo = models.ImageField('Фото')
    person_age = models.IntegerField('Возраст', default=0)
    person_bio = models.CharField('Биография', max_length=200)

    def __str__(self):
        return self.person_surname

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
