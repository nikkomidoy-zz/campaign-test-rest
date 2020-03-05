import uuid

from django.db import models
from django_countries.fields import CountryField

from campaign_test.users.models import User


class AutoDateTimeField(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TitleDescriptionBaseModel(AutoDateTimeField):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        abstract = True


class RelatedUserBaseModel(AutoDateTimeField):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Campaign(TitleDescriptionBaseModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    languages = models.ManyToManyField('Language')
    cities = models.ManyToManyField('City')

    def __str__(self):
        return self.title


class Job(TitleDescriptionBaseModel):
    price = models.FloatField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Invitation(RelatedUserBaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    ordered_keywords = models.ManyToManyField(
        'keywords.InvitationKeyword',
    )

    def __str__(self):
        return self.uuid


class Language(AutoDateTimeField):
    label = models.CharField(max_length=5)

    def __str__(self):
        return self.label


class City(AutoDateTimeField):
    name = models.CharField(max_length=32)
    country = CountryField()

    def __str__(self):
        return self.name


class Application(RelatedUserBaseModel):
    proposal = models.TextField(max_length=300)
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)

    def __str__(self):
        return self.uuid
