from django import forms
from novapp.models import Contact, UploadedDocument


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['yourname', 'youremail', 'subject', 'message']


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['title', 'document']
