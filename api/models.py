from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING

User = get_user_model()

class BaseModel(models.Model):
    """Provide default fields that are expectedly to be needed by almost all models"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    body = models.TextField(null=False, blank=False)


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=DO_NOTHING)
