from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm): # forms의 ModelForm을 상속받음

    class Meta:
        model = Jasoseol # model은 Jasoseol을 사용
        fields = ('title', 'content') # form내에 사용할 필드 정의

    # __init__: 해당 클래스가 불러질 때, 호출되는 메소드 -> 생성자
    def __init__(self, *args, **kwargs): # *args, **kwargs: 여러 인자들을 받기 위함
        super().__init__(*args, **kwargs) # super: 부모클래스에서의 기능을 사용 (여기서는 ModelForm)
        self.fields['title'].label = "제목" # name='title' 로 된 tag의 라벨 지정
        self.fields['content'].label = "자기소개서 제목" # name='content' 로 된 tag의 라벨 지정

        # name='title' 로 된 tag의 속성으로 class='jss_title', 'placeholder': '제목' 지정
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder': '제목',
        })

        # name='content' 로 된 tag의 속성으로 class='jss_content_form' 지정
        self.fields['content'].widget.attrs.update({
            'class': 'jss_content_form',
        })

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )