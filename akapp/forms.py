from django import forms
from .models import Anken, Shuho


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
        
                    
class ShuhoForm(forms.ModelForm):
    class Meta:
        model = Shuho
        fields = ('anken',
                'pub_date',
                'naiyou',
                'categori',
                'updated_at',
                )

        
        
        
        
    
    