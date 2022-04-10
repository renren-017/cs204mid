from django import forms
from chatroom.models import Message

class TextMessageForm(forms.Form):
    text_message = forms.CharField(widget=forms.Textarea(attrs={"rows":10}))
    class Meta:
        model = Message
        fields = ['content']