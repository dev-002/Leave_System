from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class applicationForm(forms.Form):
    parentEmail=forms.CharField(label="Parent's/Guardian Email ", widget = forms.EmailInput(attrs={'class': "newLine"}))
    email=forms.CharField(label="Email ", widget = forms.EmailInput(attrs={'class': "newLine"}))
    name=forms.CharField(label="Name ", widget = forms.TextInput(attrs={'class': "newLine"}))
    rollno=forms.IntegerField(label="Roll no ", widget = forms.NumberInput(attrs={'class': "newLine"}))
    phoneno=forms.IntegerField(label="Phone no ", widget = forms.NumberInput(attrs={'class': "newLine"}))
    fatherName=forms.CharField(label="Father's Name ", widget = forms.TextInput(attrs={'class': "newLine"}))
    branch=forms.CharField(label="Branch ", widget = forms.TextInput(attrs={'class': "newLine"}))
    semester=forms.CharField(label="Semester ", widget = forms.TextInput(attrs={'class': "newLine"}))
    hostelNumber=forms.CharField(label="Hostel Number ", widget = forms.TextInput(attrs={'class': "newLine"}))
    roomNumber=forms.IntegerField(label="Room Number ", widget = forms.TextInput(attrs={'class': "newLine"}))
    fromDate=forms.DateField(label="From Date ", widget = DateInput(attrs={'class': "newLine"}))
    time=forms.TimeField(label="Time ", widget = TimeInput(attrs={'class': "newLine"}))
    toDate=forms.CharField(label="To Date ", widget = DateInput(attrs={'class': "newLine"}))
    reason = forms.CharField(label="Reason ", widget = forms.Textarea(attrs={'cols':30, 'rows':5, 'class': "newLine"}))
    parentContact=forms.IntegerField(label="Parent's/Guardian Phone Number", widget=forms.NumberInput(attrs={'class': "newLine"}))