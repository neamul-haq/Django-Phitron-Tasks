from django import forms
import datetime
##https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets
class djangoForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(label="Please enter your email address",)
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    value = forms.DecimalField()
    
    email_address = forms.EmailField(required = False,)
    
    first_name = forms.CharField(initial='Rahim')
    
    agree2 = forms.BooleanField(initial=True)
    
    # for this need to : import datetime (at the beginning)
    day = forms.DateField(initial=datetime.date.today)
    
    
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]


    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    multi_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    mul_colorsCheckbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    
    ##https://www.geeksforgeeks.org/django-forms/
    password = forms.CharField(widget = forms.PasswordInput()) 
    field = forms.CharField(help_text = "Enter your Name") 
    geeks_field = forms.CharField(error_messages = {'required':"Please Enter your Name"}) 
    disable_field = forms.CharField(disabled = True) 