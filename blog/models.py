from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/" + str(self.id) + "/"

    class Meta:
        ordering = ['-id']


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"


"================== PRE SAVE and POST SAVE =============="


@receiver(pre_save, sender=Post)
def pre_save_post(sender, instance, *args, **kwargs):
    message = f"{instance.author.username} Sizni '{instance.title}' nomli postingiz yaratilishga tashlandi!"
    notification = Notification(user=instance.author, message=message)
    notification.save()


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, *args, **kwargs):
    message = f"{instance.author.username} tabriklaymiz Sizni '{instance.title}' nomli postingiz chop etildi!"

    notification = Notification(user=instance.author, message=message)
    notification.save()

# pre_save.connect(pre_save_post, sender=Post, dispatch_uid="pre_save_post")
# post_save.connect(post_save_post, sender=Post, dispatch_uid="post_save_post")
