from django import forms


class CarForm(forms.Form):
    brand = forms.CharField()
    model = forms.CharField()
    color = forms.CharField()
    year = forms.IntegerField()

    def do_action(self):
        print("액션을 하였습니당.")
