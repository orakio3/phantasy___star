from django.db import models

class Platform(models.Model):

    TYPE_SEGA = 0
    TYPE_PS1 = 1
    TYPE_PS2 = 2
    TYPE_PS3 = 3
    TYPE_XBOX360 = 4
    TYPE_PC = 5
    TYPE_GEAR = 6
    TYPE_VITA = 7
    TYPE_DS = 8
    TYPE_PSP = 9
    TYPE_DREAMCAST = 10

    TYPE_CHOICES = (
        (TYPE_SEGA, 'Sega Mega Drive'),
        (TYPE_PS1, 'Sony Playstation'),
        (TYPE_PS2, 'Sony Playstation 2'),
        (TYPE_PS3, 'Sony Playstation 3'),
        (TYPE_XBOX360, 'X-Box 360'),
        (TYPE_PC, 'PC'),
        (TYPE_GEAR, 'GameGear'),
        (TYPE_VITA, 'VITA'),
        (TYPE_DS, 'DS'),
        (TYPE_PSP, 'PSP'),
        (TYPE_DREAMCAST, 'DREAMCAST')
    )

    name = models.CharField(max_length=255, default=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_SEGA)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Game(models.Model):

    title = models.CharField(max_length=255, null=True)
    summary = models.TextField(null=True)
    release = models.DateField(null=True)
    platforms = models.ForeignKey('main.Platform', default=True, on_delete=models.CASCADE)
    faq = models.TextField(null=True,blank=True)
    genre = models.ManyToManyField('main.Genre')
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Genre(models.Model):

    TYPE_JRPG = 0
    TYPE_ACTIONRPG = 1
    TYPE_MMORPG = 2

    TYPE_CHOICES = (

        (TYPE_JRPG, 'JRPG'),
        (TYPE_ACTIONRPG, 'Action-RPG'),
        (TYPE_MMORPG, 'MMORPG')

    )
    name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    new = models.ForeignKey('game', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

