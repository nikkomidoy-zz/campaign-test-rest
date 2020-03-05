import uuid

from django.db import models

from campaigns.models import AutoDateTimeField


class Keyword(AutoDateTimeField):
    label = models.CharField(max_length=32)

    def __str__(self):
        return self.label


class InvitationKeyword(AutoDateTimeField):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.keyword


class UserKeyword(AutoDateTimeField):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.keyword
