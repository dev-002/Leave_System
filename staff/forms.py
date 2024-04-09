from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class applicationForm(forms.Form):
    phoneno=forms.IntegerField(label="Phone no ", widget = forms.NumberInput(attrs={'class': "newLine"}))
    fromDate=forms.DateField(label="From Date ", widget = DateInput(attrs={'class': "newLine"}))
    toDate=forms.CharField(label="To Date ", widget = DateInput(attrs={'class': "newLine"}))
    reason = forms.CharField(label="Reason ", widget = forms.Textarea(attrs={'cols':30, 'rows':5, 'class': "newLine"}))