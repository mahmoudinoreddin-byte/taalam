from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def other_participant(self, user):
        return self.participants.exclude(pk=user.pk).first()

    def last_message(self):
        return self.messages.last()

    def unread_count(self, user):
        return self.messages.filter(is_read=False).exclude(sender=user).count()

    def __str__(self):
        return f'Conversation #{self.pk}'


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sender.username}: {self.body[:40]}'
