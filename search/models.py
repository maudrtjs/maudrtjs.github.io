from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

import datetime


class Sheet(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='unknown')
    compositor = models.CharField(max_length=42, default='unknown')
    instrumentation = models.CharField(max_length=155, default='unknown')
    pdf_link = models.URLField(max_length=200, default='unknown')
    sections = models.CharField(max_length=100, default='unknown')
    description = models.CharField(max_length=100, default='unknown')
    composition_date = models.IntegerField(default=0)
    first_interpretation_date = models.CharField(max_length=100, default='unknown')
    release_date = models.CharField(max_length=100, default='unknown')
    duration = models.CharField(max_length=100, default='unknown')
    compositor_period = models.CharField(max_length=100, default='unknown')
    editor = models.CharField(max_length=100, default='unknown')
    style = models.CharField(max_length=100, default='unknown')
    key = models.CharField(max_length=100, default='unknown')
    source = models.CharField(max_length=100, default='unknown')
    comments = models.CharField(max_length=1000, default='no comment')
    nb_instruments = models.IntegerField(default=0)
    difficulty = models.FloatField(default=0)
    popularity = models.FloatField(default=0)
    dedication = models.CharField(max_length=100, default='unknown')
    num_opus = models.CharField(max_length=100, default='unknown')
    download_date = models.DateTimeField(default=timezone.now,
                                verbose_name="Publication date",
                                null=True)
    commentaires = GenericRelation('Commentaire')

    class Meta:
        verbose_name = "Music score"
        ordering = ['title']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.title



class Commentaire(models.Model):
    autor = models.CharField(max_length=255)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "Comment of {0} aboout {1}".format(self.auteur, self.content_object)