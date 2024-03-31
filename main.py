from django.db import models
adress = models.CharField(max_length=256, blank=False)
class Address(models.Model):
    si = models.CharField(max_length=32)
    do = models.CharField(max_length=32)
    gu = models.CharField(max_length=64)
    detail = models.CharField(
        max_length=128,
        help_text="사용자가 입력한 정식 주소체계 이외 상세주소"
    )