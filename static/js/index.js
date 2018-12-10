$(document).ready(function () {
    var is_nav_li = false;
    //分类子菜单的显示与隐藏
    $(".nav-li").mouseenter(function(){
        is_nav_li = false;
      var nav_li_index = $(this);
        $(".category-nav-detail").eq(nav_li_index.index()).addClass("active");
        // $(".category-nav-container").style(display="block");
        $(".category-nav-detail-wrapper").css("display", "block");
        $(".category-nav-detail").eq(nav_li_index.index()).siblings().removeClass("active");
    });

    $(".nav-li").mouseleave(function() {
          $(".category-nav-detail-wrapper").mouseenter(function () {
            $(".category-nav-detail-wrapper").css("display", "block");
            is_nav_li = true
            });

          if (!is_nav_li){
              $(".category-nav-detail-wrapper").css("display", "none");
          }else {
              $(".category-nav-detail-wrapper").css("display", "block");
          }
        });

    $(".category-nav-detail-wrapper").mouseleave(function () {
        is_nav_li = false;
        $(".category-nav-detail-wrapper").css("display", "none");
    })

});