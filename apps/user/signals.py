from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import User, Notification
from apps.blog.models import Like, Comment

@receiver(post_save, sender=User)
def send_user_notification(sender, instance, created, **kwargs):
    if created:
        message = f"Новый пользователь создан: {instance.email}"
        Notification.objects.create(user=instance, message=message)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": message
            }
        )

@receiver(post_save, sender=Like)
def send_like_notification(sender, instance, created, **kwargs):
    if created:
        message = f"Пользователь {instance.user.email} лайкнул блог {instance.blog.title}"
        Notification.objects.create(user=instance.blog.user, message=message)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": message
            }
        )

@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, created, **kwargs):
    if created:
        message = f"Пользователь {instance.user.email} оставил комментарий к блогу {instance.blog.title}: {instance.text}"
        Notification.objects.create(user=instance.blog.user, message=message)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "public_room",
            {
                "type": "send_notification",
                "message": message
            }
        )

@receiver(post_save, sender=Notification)
def notification_created(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'public_room',
            {
                "type": "send_notification",
                "message": instance.message
            }
        )
