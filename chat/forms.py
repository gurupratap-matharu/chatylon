from django import forms

from chat.models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }
