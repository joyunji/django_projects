from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime


# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션이라는 것을 만든다. 
# 이 모델에 맞는 테이블 생성한다.
# 질문: 여름에 놀러간다면 어디에 갈래?
# 산
# 강
# 바다
# 도심 호캉스

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name ='질문') # 질문내용
    pub_data = models.DateTimeField(auto_now_add=True, verbose_name ='생성일') # 생성날짜
    
    @admin.display(boolean = True, description='최근 생성(하루기준)')
    def was_published_recently(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        if self.was_published_recently():
            new_bage = 'NEW!!'
        else:
            new_bage = ''
        return f'{new_bage} 제목: {self.question_text}, 날짜:{self.pub_data}'
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'[{self.question.question_text}]{self.choice_text}'  
    
    