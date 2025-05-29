# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Referral
from django.conf import settings


@receiver(post_save, sender=Referral)
def notify_referrer(sender, instance, created, **kwargs):
    if not created:
        return
    ref = instance.referrer
    new_user = instance.referred
    send_mail(
        subject="🎉 You've got a new referral!",
        message=(
            f"Hey {ref.first_name},\n\n"
            f"{new_user.first_name} just signed up with your referral code.\n"
            "Your bonus has been applied.\n\n"
            "Keep sharing!\n"
            "— Hedgeon Finance Capital"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[ref.email],
    )
