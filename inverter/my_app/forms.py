from django import forms

class ReportForm(forms.Form):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '1'}),  # 'step' allows seconds
        label="Start Time"
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '1'}),  # 'step' allows seconds
        label="End Time"
    )
    interval_type = forms.ChoiceField(
        choices=[
            ('minute', 'Minute'),
            ('hour', 'Hour'),
            ('day', 'Day'),
            ('month', 'Month'),
        ],
        label="Interval Type"
    )
    interval_duration = forms.IntegerField(
        label="Duration",
        min_value=1,
    )