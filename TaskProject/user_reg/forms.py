from datetime import date, datetime

from django import forms
from django.forms import ModelForm

from dateutil import parser
from dateutil.relativedelta import relativedelta

from .models import User


class UserRegForm(ModelForm):
    def clean(self):
        cleaned_data = super(UserRegForm, self).clean()
        birth_date = cleaned_data.get('birth_date')
        if birth_date:
            # birth_date in future
            if datetime.now().date() <= birth_date:
                msg = u"u are in the future"
                self.add_error('birth_date', msg)
            # under 18 check
            today = date.today()
            today_minus_18y = date.today() - relativedelta(years=18)
            if birth_date > today_minus_18y:
                msg = u"You are under 18years dude!"
                self.add_error('birth_date', msg)
        return cleaned_data

    class Meta:
        model = User
        fields = ['full_name', 'email', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(format=('%Y/%d/%m'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

