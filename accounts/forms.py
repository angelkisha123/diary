from django.forms import ModelForm
from .models import Member
from .models import Chapter

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'