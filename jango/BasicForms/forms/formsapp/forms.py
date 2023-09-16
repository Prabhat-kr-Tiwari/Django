from django import forms
class NameForm(forms.Form):
    your_name=forms.CharField(max_length=10)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)