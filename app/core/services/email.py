"""
Serviço de envio de e-mail.
"""
from decouple import config
from django.core.mail import EmailMessage, send_mass_mail


def send_mail():
    ...


def create_email_message(instance, email):
    message = EmailMessage(
        subject=instance.titulo,
        body=instance.mensagem,
        from_email=config('FROM_EMAIL'),
        to=['lista_de_emails_a_partir_de_um_filtro@example.com'],
        bcc=[email],
    )
    return (
        message.subject,
        message.body,
        message.from_email,
        message.recipients(),
    )


def service_send_mass_mail(instance):
    """
    Dica: usar em um gerenciador de filas, Celery por exemplo.

    Envia e-mail em massa.
    https://docs.djangoproject.com/en/5.0/topics/email/#send-mass-mail
    """
    emails = instance.emails.split(', ')
    messages = [create_email_message(instance, email) for email in emails]
    send_mass_mail(messages, fail_silently=False)
