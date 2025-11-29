from django import forms

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="nickname", max_length=50)
    message_input = forms.CharField(label="message", max_length=500)
