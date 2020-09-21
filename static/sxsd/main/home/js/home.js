
$(function () {
    init_newSwiper()
    init_swiperMenu()
})
//初始化轮播图
function init_newSwiper() {
     var newSwiper = new Swiper(
         '#topSwiper',{
             loop:true,
             autoplay:3000,
             autoplayDisableOnInteraction:false,
             pagination:'.swiper-pagination'
         }
     )
}

//初始化必买
function init_swiperMenu() {
    var newSwiper1 = new Swiper(
        '#swiperMenu',{
            slidesPerView :3
        }
    )
}
