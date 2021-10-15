from django import forms
from .models import Anken, Shuho
import bootstrap_datepicker_plus as datetimepicker
from django_summernote.widgets import SummernoteWidget



class AnkenForm(forms.ModelForm):
    class Meta:
        model = Anken
        fields = ('pub_date',
                'ankenmei',
                'iraibusho',
                'iraisha',
                'nouki',
                'mitumorikousu',
                'naiyou',
                'genjouchi', 
                'kitaikouka', 
                'tantousha',  
                'koumoku', 
                'joutai', 
                'jissekikousu',
                'updated_at',
                )
        widgets = {
            'nouki': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'naiyou': SummernoteWidget(),
        }
        
                    
class ShuhoForm(forms.ModelForm):
    class Meta:
        model = Shuho
        fields = ('anken',
                'pub_date',
                'naiyou',
                'categori',
                'updated_at',
                )
        widgets = {
            'naiyou': SummernoteWidget(),
        }

        
        
        
        
    
    