from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Conversation, Message

User = get_user_model()

@login_required
def inbox(request):
    conversations = request.user.conversations.prefetch_related('participants', 'messages').order_by('-updated_at')
    # Annotate unread counts
    conv_data = []
    for conv in conversations:
        other = conv.other_participant(request.user)
        last = conv.last_message()
        unread = conv.unread_count(request.user)
        conv_data.append({'conv': conv, 'other': other, 'last': last, 'unread': unread})
    total_unread = sum(c['unread'] for c in conv_data)
    return render(request, 'messaging/inbox.html', {
        'conv_data': conv_data,
        'total_unread': total_unread,
    })

@login_required
def conversation(request, conv_id):
    conv = get_object_or_404(Conversation, pk=conv_id, participants=request.user)
    # Mark all messages in this conversation as read
    conv.messages.exclude(sender=request.user).update(is_read=True)
    messages_list = conv.messages.select_related('sender').all()
    other = conv.other_participant(request.user)
    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if body:
            Message.objects.create(conversation=conv, sender=request.user, body=body)
            conv.save()  # update updated_at
        return redirect('conversation', conv_id=conv.pk)
    return render(request, 'messaging/conversation.html', {
        'conv': conv,
        'messages_list': messages_list,
        'other': other,
    })

@login_required
def start_conversation(request, username):
    other = get_object_or_404(User, username=username)
    if other == request.user:
        return redirect('inbox')
    # Find existing conversation between these two users
    conv = Conversation.objects.filter(participants=request.user).filter(participants=other).first()
    if not conv:
        conv = Conversation.objects.create()
        conv.participants.add(request.user, other)
    return redirect('conversation', conv_id=conv.pk)

@login_required
def delete_conversation(request, conv_id):
    conv = get_object_or_404(Conversation, pk=conv_id, participants=request.user)
    conv.delete()
    return redirect('inbox')
