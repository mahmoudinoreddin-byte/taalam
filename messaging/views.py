from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages as django_messages
from .models import Message

User = get_user_model()

@login_required
def inbox(request):
    msgs = Message.objects.filter(recipient=request.user).select_related('sender')
    unread_count = msgs.filter(is_read=False).count()
    return render(request, 'messaging/inbox.html', {'messages_list': msgs, 'unread_count': unread_count})

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk, recipient=request.user)
    if not msg.is_read:
        msg.is_read = True
        msg.save()
    return render(request, 'messaging/message_detail.html', {'msg': msg})

@login_required
def send_message(request, username=None):
    recipient = None
    if username:
        recipient = get_object_or_404(User, username=username)
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        try:
            to_user = User.objects.get(username=recipient_username)
            Message.objects.create(sender=request.user, recipient=to_user, subject=subject, body=body)
            django_messages.success(request, f'Message sent to {to_user.username}!')
            return redirect('inbox')
        except User.DoesNotExist:
            django_messages.error(request, 'User not found.')
    return render(request, 'messaging/compose.html', {'recipient': recipient})

@login_required
def delete_message(request, pk):
    msg = get_object_or_404(Message, pk=pk, recipient=request.user)
    msg.delete()
    return redirect('inbox')
