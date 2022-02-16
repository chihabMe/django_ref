from django import forms 
from .models import Article
class ArticleCreatForm(forms.ModelForm):
    class Meta:
        model = Article
        fields  = ['title','body']
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title=title)
        if qs.exists():
            self.add_error("title",f"this title '{title}' is already in use")
        return data 

# class ArticleCreatForm(forms.Form):
#     title = forms.CharField()
#     body = forms.CharField()

#     def clean_title(self):
#         cleaned_title = self.cleaned_data
#         print(cleaned_title)
#         title = cleaned_title.get("title")
#         if title.lower().strip()=="lol":
#             raise forms.ValidationError("we dont do this here !")
#         print("title",title)
#         return title