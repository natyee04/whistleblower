from django import forms
from .models import Report, File

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["report_text", "status"]


class FileForm(forms.Form): # not a ModelForm since uploading multiple files
    file_fileds = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)