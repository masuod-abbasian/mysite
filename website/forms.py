
from django import forms
from django.forms.widgets import Textarea
from website.models import Contact , Newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email= forms.EmailField()
    subject = forms.CharField(max_length=255,required=False)
    message = forms.CharField(widget=forms.Textarea)

class Contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Contactform, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False

class Newsletterform(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'