from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Chat, Message
from django.contrib.auth.models import User
from django.db.models import Q


@login_required
def chat_list(request):
    chats = Chat.objects.filter(Q(utente1=request.user) | Q(utente2=request.user))
    return render(request, 'chat/chat_list.html', {'chats': chats})

@login_required
def create_chat(request, user_id):
    other_user = User.objects.get(id=user_id)

    if not Chat.objects.filter(utente1=request.user, utente2=other_user).exists():
        chat = Chat(utente1=request.user, utente2=other_user)
        try:
            chat.save()
        except Exception as e:
            messages.error(request, "Abbiamo riscontrato un problema durante la creazione della chat")
            return redirect('home')
    else:
        chat = Chat.objects.get(utente1=request.user, utente2=user_id)

    return redirect('chat:chat_view', chat_id=chat.id)



@login_required
def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.user != chat.utente1 and request.user != chat.utente2:
        return HttpResponseForbidden()

    messages = chat.messages.all()
    return render(request, 'chat/chat_view.html', {'chat': chat, 'messages': messages})