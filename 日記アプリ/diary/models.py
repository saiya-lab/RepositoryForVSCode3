from django.db import models
from pathlib import Path
import uuid

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")#日記のページを一意に識別するためのカラム
    title = models.CharField(max_length=100, verbose_name="タイトル")
    body = models.TextField(max_length=200, verbose_name= "本文")
    page_date = models.DateField(verbose_name="日付")
    picture = models.ImageField(
        upload_to="diary/picture/", blank=True, null=True, verbose_name="写真")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")#このデータが初めて作成されたその時の日時を保存
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)

# Create your models here.
#代表的なフィールド
#integerFiled→数値
#EmailField→メールアドレス
#FloatField→小数点を含む数値
#BooleanField→True/False
#ImageField→画像
#FoerignKey→外部キー