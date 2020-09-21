from django.shortcuts import render

# Create your views here.
from MarketApp.models import SxsdFoodType, SxsdGoods


def market(request):
    info = {}
    # composite_sort_list = [ '综合排序': 0,'价格升序': 1,'价格降序': 2,'销量升序': 3,'销量降序': 4]
    composite_sort_list = ['综合排序','价格升序','价格降序','销量升序','销量降序']

    typeid = request.GET.get('typeid','104749')  # 产品类型id 根据产品id显示不同的产品
    childcid = request.GET.get('childcid','0')  # 同一产品类型中不同的子产品 二级联动查询产品
    # price = request.GET.get('price','asc')  # 产品的价格 用来进行对产品价格的升序和降序判断
    # productnum = request.GET.get('productnum','desc')  # 产品销量 用来对产品销量的排序

    sort = request.GET.get('sort','0')
    if sort.isdigit():
        sort = int(sort)
        if sort > 4:
            sort = 0
    else:
        sort = 0

    foodtypes = SxsdFoodType.objects.all()  # 获取market左栏的数据
    if typeid.isdigit():
        '''判断用户是否随便输入typeid'''
        typeids = []
        for foodtype in foodtypes:
            typeids.append(foodtype.typeid)
        if typeid not in typeids:
            info['categoryid'] = '104749'
        else:
            info['categoryid'] = typeid
    else:
        info['categoryid'] = '104749'


    if childcid.isdigit(): # 判断childcid是否是纯数字
        '''二级联动查询，判断客户是否进行二级查询'''
        if childcid != '0':
            info['childcid'] = childcid

    # if price:
    #     '''三级联动查询，判断客户是否进行三级查询'''
    #     if price == 'asc':
    #         goods = SxsdGoods.objects.filter(**info).order_by('price')
    #     else:
    #         goods = SxsdGoods.objects.filter(**info).order_by('-price')
    # elif productnum:
    #     if productnum == 'asc':
    #         goods = SxsdGoods.objects.filter(**info).order_by('productnum')
    #     else:
    #         goods = SxsdGoods.objects.filter(**info).order_by('-productnum')
    # elif price and productnum:
    #     goods = SxsdGoods.objects.filter(**info).order_by(('-productnum','price'))
    # else:
    #     goods = SxsdGoods.objects.filter(**info)

    if sort == 0:
        '''三级联动查询，判断客户是否进行三级查询'''
        goods = SxsdGoods.objects.filter(**info).order_by('-productnum','price')
    elif sort == 1:
        goods = SxsdGoods.objects.filter(**info).order_by('price')
    elif sort == 2:
        goods = SxsdGoods.objects.filter(**info).order_by('-price')
    elif sort == 3:
        goods = SxsdGoods.objects.filter(**info).order_by('productnum')
    elif sort == 4:
        goods = SxsdGoods.objects.filter(**info).order_by('-productnum')
    else:
        goods = SxsdGoods.objects.filter(**info)



    # 二级查询的信息 第一种获取方式
    # all_type_names = SxsdGoods.objects.filter(categoryid=typeid).values('childcid','childcidname').distinct()

    # 二级查询的信息 第二种获取方式
    all_type_infos = SxsdFoodType.objects.filter(typeid=typeid)
    all_infos = []
    for all_infos1 in all_type_infos:
        all_infos2 = all_infos1.childtypenames.split('#')
        for all_infos3 in all_infos2:
            all_infos.append(all_infos3.split(":"))

    context = {
        'foodtypes':foodtypes,
        'typeid':typeid,
        'goods':goods,
        # 'all_type_names':all_type_names,
        'all_infos':all_infos,
        'childcid':childcid,
        'composite_sort_list':composite_sort_list,
        'sort':sort,



    }
    return render(request,'sxsd/main/market/market.html',context=context)