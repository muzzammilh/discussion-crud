from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING

from django.db.models import signals
from django.dispatch import receiver

User = get_user_model()

class BaseModel(models.Model):
    '''Provide default fields that are expectedly to be needed by almost all models'''

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    body = models.TextField(null=False, blank=False)
    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User, related_name='user_likes', null=True, blank=True)


@receiver(signals.m2m_changed, sender=Post.user_likes.through)
def update_likes_count(instance, action, pk_set, **kwargs):
    if action == 'post_add':
        instance.likes += len(pk_set)
        instance.save()
