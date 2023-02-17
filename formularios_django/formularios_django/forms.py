from socket import fromshare
from django import forms

class CommentForm(forms.Form):
    name= forms.CharField(label="Escribe tu nombre", max_length=10, help_text="10 caracteres maximo")
    url= forms.URLField(label= "Tu sitio web", required=False,initial='http//:')
    comment= forms.CharField()

class ContactForm(forms.Form):
    name= forms.CharField(label="Nombre:",
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(label= "Email", required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    messasge= forms.CharField(label= "Mensaje",widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_name(self):
        name= self.cleaned_data.get("name")
        if name != "Open":
            raise forms.ValidationError("Tan solo el valor OPen esta permitido")
        else:
            return name
