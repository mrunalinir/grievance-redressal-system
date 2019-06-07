from django import forms

class Grievance_form(forms.Form):
    main_content=forms.CharField()
    department= forms.ChoiceField(choices=[('department1','Department1'), ('department2','Department2'), ('others','Others')])
