from django.forms import ModelForm, CharField, ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    name = CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['name', 'age', 'blood_group', 'home_address', 'city', 'hospital_distance', 'phone_number', 'phone_number_2', 'is_donor']

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            label_text = self.fields[field].label or field.replace('_', ' ').title()
            placeholder_text = f"e.g. {label_text}"
            self.fields[field].widget.attrs.update({
                'class': 'form-input',
                'placeholder': placeholder_text
            })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if User.objects.filter(name__iexact=name).exists():
            raise ValidationError("A user with that name already exists.")
        return name


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-input'})


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'home_address', 'blood_group', 'city', 'hospital_distance', 'phone_number', 'phone_number_2', 'is_donor']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            label_text = self.fields[field].label or field.replace('_', ' ').title()
            placeholder_text = f"e.g. {label_text}"
            self.fields[field].widget.attrs.update({
                'class': 'form-input',
                'placeholder': placeholder_text
            })
