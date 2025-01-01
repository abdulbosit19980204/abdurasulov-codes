from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from blog.models import Post, Notification, VisitorsAddressModel

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
# @receiver(pre_save, sender=VisitorsAddressModel)
# def user_add_ip_pre_save(sender, instance, *args, **kwargs):
#     instance.user = instance.request.user
#     instance.ip = instance.request.META.get('REMOTE_ADDR')
