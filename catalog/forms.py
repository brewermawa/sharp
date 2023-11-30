from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        labels = {
            "name":  "Nombre",
            "phone": "Teléfono",
            "message": "Comentario",
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["phone"].required = False
        self.label_suffix = ""