# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from .models import Chat, Message
from django.contrib.auth.models import User


@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    return render(request, 'chat/user_list.html', {'users': users})

@login_required
def create_chat(request, user_id):
    other_user = User.objects.get(id=user_id)
    chat = Chat.objects.create()
    chat.participants.add(request.user, other_user)
    chat.save()
    return redirect('chat_view', chat_id=chat.id)

@login_required
def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.user not in chat.participants.all():
        return HttpResponseForbidden()

    messages = chat.messages.all()
    return render(request, 'chat/chat_view.html', {'chat': chat, 'messages': messages})