from django.db import models
from django.utils import timezone


class Anken(models.Model):
    TANTOUSHA_CHOICES = (
                        ("0", "Aさん"),
                        ("1", "Bさん"),
                        ("2", "Cさん"),
                        )

    KOUMOKU_CHOICES = (
                        ("0", "案件"),
                        ("1", "案件_別途報告"),
                        ("2", "創意工夫展開"),
                        ("3", "自己研鑽"),
                        ("4", "お知らせ"),
                        ("5", "その他"),
                        )

    JOUTAI_CHOICES = (
                        ("0", "対応中"),
                        ("1", "完了"),
                        ("2", "一時休止"),
                        ("3", "未着手"),
                        ("4", "指定しない"),
                        )

    pub_date = models.DateTimeField(verbose_name='日付',default=timezone.now)
    ankenmei = models.CharField(verbose_name='案件名',max_length=200)
    iraibusho = models.CharField(verbose_name='依頼部署',max_length=200)
    iraisha = models.CharField(verbose_name='依頼者',max_length=200)
    nouki = models.DateTimeField(verbose_name='納期')
    mitumorikousu = models.IntegerField(verbose_name='見積工数(H)',default=0)
    naiyou = models.TextField(verbose_name='内容',max_length=1000)
    genjouchi = models.CharField(verbose_name='現状値',max_length=200)
    kitaikouka = models.CharField(verbose_name='期待効果',max_length=200)
    tantousha = models.CharField(verbose_name='担当者',choices=TANTOUSHA_CHOICES,max_length=200)
    koumoku = models.CharField(verbose_name='項目',choices=KOUMOKU_CHOICES,max_length=200)
    joutai = models.CharField(verbose_name='状態',choices=JOUTAI_CHOICES,max_length=200)
    jissekikousu = models.IntegerField(verbose_name='実績工数(H)',default=0)
    updated_at = models.DateTimeField(verbose_name='更新日時',blank=True, null=True)

    def __str__(self):
        return self.ankenmei


class Shuho(models.Model):
    CATEGORI_CHOICES = (
                            ("0", "環境構築"),
                            ("1", "前処理"),
                            ("2", "分析手法"),
                            ("3", "エッジ・設備"),
                            ("4", "その他"),
                        )

    anken = models.ForeignKey(Anken, verbose_name='案件',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name='日付',default=timezone.now)
    naiyou = models.TextField(verbose_name='内容',max_length=1000)
    categori = models.CharField(verbose_name='カテゴリ',choices=CATEGORI_CHOICES,max_length=200)
    updated_at = models.DateTimeField(verbose_name='更新日時',blank=True, null=True)

    def __str__(self):
        return self.anken
