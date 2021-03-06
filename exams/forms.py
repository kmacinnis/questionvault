from django import forms
from django.forms.models import inlineformset_factory


from exams.models import *


from utils.forms import CLASS_CONTROL


class ExamRecipeForm(forms.ModelForm):
    class Meta:
        model = ExamRecipe
        fields = (
            'course',
            'private_title',
            'display_title',
            'form_number_style',
            'number_of_forms',
            'max_number_choices',
        )


PartRecipeFormSet = inlineformset_factory(
    ExamRecipe,
    ExamPartRecipe,
    fields = '__all__',
)


class PartRecipeForm(forms.ModelForm):
    class Meta:
        model = ExamPartRecipe
        fields = (
            'title',
            'show_title',
            'instructions',
            'question_style',
            'shuffled',
        )
        labels = {
            'shuffled' : 'shuffle questions in this part',
        }
        widgets = {
            'title' : forms.TextInput(attrs=CLASS_CONTROL),
            'instructions' : forms.Textarea(attrs=CLASS_CONTROL),
            # 'show_title' : forms.CheckboxInput(attrs=CLASS_CONTROL),
        }

class ExamQuestionInlineForm(forms.ModelForm):
    class Meta:
        model = ExamRecipeQuestion
        fields = (
            'order',
            'question',
            'name',
            'question_style',
            'space_after',
        )
        widgets = {
            'question': forms.HiddenInput(),
            'order': forms.HiddenInput(),
            'space_after': forms.TextInput(attrs=CLASS_CONTROL),
            'name': forms.HiddenInput(),
            'question_style': forms.Select(attrs={'class':'small-select'}),
            
        }


QuestionInlineFormSet = inlineformset_factory(
    ExamPartRecipe,
    ExamRecipeQuestion,
    form = ExamQuestionInlineForm,
    extra = 0,
)





# class ExamPoolInlineForm(forms.ModelForm):
#     class Meta:
#         model = ExamRecipePool
#         fields = (
#             'order',
#             'choose',
#             'name',
#             'question_style',
#             'space_after',
#         )
#         widgets = {
#             'question': forms.HiddenInput(),
#             'order': forms.HiddenInput(),
#             'space_after': forms.TextInput(attrs=CLASS_CONTROL),
#             'name': forms.TextInput(attrs=CLASS_CONTROL),
#             'question_style': forms.Select(attrs={'class':'small-select'}),
#             'choose':forms.TextInput(attrs=CLASS_CONTROL)
#         }

class PoolForm(forms.ModelForm):
    # pool_id = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = ExamRecipePool
        fields = (
            'id',
            'part',
            'order',
            'name',
            'question_style',
            'space_after',
            'choose',
        )
        widgets = {
            'id' : forms.TextInput(),
            'part' : forms.HiddenInput(),
            'order' : forms.HiddenInput(),
            'space_after': forms.TextInput(attrs=CLASS_CONTROL),
            'name' : forms.TextInput(attrs=CLASS_CONTROL),
            'choose' : forms.TextInput(attrs=CLASS_CONTROL),            
        }

class ItemMiniForm(forms.ModelForm):
    class Meta:
        model = ExamRecipeQuestion
        fields = (
            'question_style',
            'space_after',
        )
    

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = FormattingPreferences
        fields = '__all__'
        widgets = {
            'user' : forms.HiddenInput(),
        }

