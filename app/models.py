from django.db import models


class Games(models.Model):
    team1 = models.CharField(max_length=255)
    team2 = models.CharField(max_length=255)
    result = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return f'Игра номер {self.id}'


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    @property
    def first_photo(self):
        return self.photos.first().photo.url if self.photos.exists() else None


class NewsPhoto(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='news_images')

    class Meta:
        verbose_name = 'Фотка новости'
        verbose_name_plural = 'Фотки новости'

    def __str__(self):
        return f'Фотка новости - {self.news.title}'


class BackgroundPhoto(models.Model):
    photo = models.ImageField(upload_to='background_images')

    class Meta:
        verbose_name = 'Фотка фона'
        verbose_name_plural = 'Фотки фона'

    def __str__(self):
        return f'Фотка фона номер {self.id}'
