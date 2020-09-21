from django.db import models

# Create your models here.
from MarketApp.models import SxsdGoods
from UserApp.models import SxsdUser


class SxsdOrder(models.Model):
    o_user = models.ForeignKey(SxsdUser)
    o_time = models.DateTimeField(auto_now_add=True)
    o_total_price = models.IntegerField()

    class Meta:
        db_table = 'sxsd_order'

class SxsdOrderGoods(models.Model):
    og_order = models.ForeignKey(SxsdOrder)
    og_goods = models.ForeignKey(SxsdGoods)
    og_c_goods_num = models.IntegerField()

    class Meta:
        db_table = 'sxsd_orderGoods'
