from django.db import models

# Create your models here.
# axf_foodtype
# (typeid,typename,childtypenames,typesort)
# values("104749","热销榜","全部分类:0",1)

class SxsdFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=128)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'sxsd_foodtype'

# axf_goods (
# id, productid, productimg, productname, productlongname,
# isxf, pmdesc, specifics, price, marketprice,
# categoryid, childcid, childcidname, dealerid, storenums, productnum)
# VALUES
# (830, 11947, '/media/images/goods023.png', '', '乐吧薯片芝士味50.0g',
# 0, 0, '50g', 2, 2.5,
# 103541, 103543, '膨化食品', 4858, 200, 4);

class SxsdGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=64)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=128)

    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()

    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=32)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'sxsd_goods'


