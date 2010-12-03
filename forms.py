from django import forms

class RatingForm(forms.Form):
    score = forms.IntegerField()

class PerPageForm(forms.Form):
    perpage = forms.IntegerField()

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

class UserExtraForm(forms.Form):
    institution = forms.CharField()
    firstname = forms.CharField(
        label='Given Name',
    )
    lastname = forms.CharField(
        label='Surname',
    )
    email = forms.EmailField()
