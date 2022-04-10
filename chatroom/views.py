from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Message
from .forms import TextMessageForm
from django.contrib import messages

def home(request):
    context = {
        'text_messages': Message.objects.all()
    }
    return render(request, 'chatroom\home.html', context)

class MessageListView(ListView):
    model = Message
    template_name = 'chatroom/home.html'
    context_object_name = 'text_messages'
    ordering = ['-posted_on']

def get_message(request):
    if request.method == 'POST':
        form = TextMessageForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                text_message = form.cleaned_data.get('text_message')
                request.user.message_set.create(username=request.user.username, content=text_message)
                return redirect('chatroom-home')
            else:
                return redirect('login')
    else:
        form = TextMessageForm()
    query_set = Message.objects.order_by('-posted_on')
    context = {'form':form, 'text_messages':query_set}
    return render(request, 'chatroom/home.html', context)