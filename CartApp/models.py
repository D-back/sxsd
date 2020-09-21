from django.db import models

# Create your models here.
from MarketApp.models import SxsdGoods
from UserApp.models import SxsdUser


class SxsdCart(models.Model):
    c_user = models.ForeignKey(SxsdUser)
    c_goods = models.ForeignKey(SxsdGoods)
    c_is_select = models.BooleanField(default=0)
    c_goods_num = models.IntegerField()

    class Meta:
        db_table = 'sxsd_cart'

