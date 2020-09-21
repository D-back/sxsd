from django.db import models

# Create your models here.
#axf_wheel (id, img, name, trackid)
# (1, '/media/images/ad02.jpg', '酸奶女王', 21870);
class Sxsd(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    class Meta:
        abstract = True


class SxsdWheel(Sxsd):
    class Meta:
        db_table = 'sxsd_wheel'


class SxsdNav(Sxsd):
    class Meta:
        db_table = 'sxsd_nav'

class SxsdMustbuy(Sxsd):
    class Meta:
        db_table = 'sxsd_mustbuy'

 # axf_mainshow
# (id, img, name, trackid, categoryid, brandname,
# img1, childcid1, productid1, longname1, price1, marketprice1,
# img2, childcid2, productid2, longname2, price2, marketprice2,
# img3, childcid3, productid3, longname3, price3, marketprice3)
# VALUES
# (1, '/media/images/ad01.jpg', '优选水果', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);

class SxsdMainShow(Sxsd):
    categoryid = models.CharField(max_length=32)
    brandname = models.CharField(max_length=32)
    img1 = models.CharField(max_length=64)
    childcid1 = models.CharField(max_length=32)
    productid1 = models.CharField(max_length=32)
    longname1 = models.CharField(max_length=32)
    price1 = models.CharField(max_length=32)
    marketprice1 = models.CharField(max_length=32)
    img2 = models.CharField(max_length=64)
    childcid2 = models.CharField(max_length=32)
    productid2 = models.CharField(max_length=32)
    longname2 = models.CharField(max_length=32)
    price2 = models.CharField(max_length=32)
    marketprice2 = models.CharField(max_length=32)
    img3 = models.CharField(max_length=64)
    childcid3 = models.CharField(max_length=32)
    productid3 = models.CharField(max_length=32)
    longname3 = models.CharField(max_length=32)
    price3 = models.CharField(max_length=32)
    marketprice3 = models.CharField(max_length=32)

    class Meta:
        db_table = 'sxsd_mainshow'