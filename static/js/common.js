$(document).ready(function () {
  $("#gotop").click(function () {
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      400
    );
    return false;
  });

  $("#main_menuicon, #menuicon").click(function () {
    $(".sidebar").css({
      display: "block",
      opacity: "1",
    });
    $(".sidebar").animate({ top: "0px" }, 800);
  });

  $("#top_category").mouseenter(function () {
    $("#top_category_sub").css("display", "block");
    return false;
  });

  $("#top_category_sub").mouseleave(function () {
    $("#top_category_sub").fadeOut();
    return false;
  });

  $("#perinfo_bottom").click(function () {
    $("#perinfo").show();
    return false;
  });

  $("#right_bottom").click(function () {
    $("#right").show();
    return false;
  });

  $("#nonpay_bottom").click(function () {
    $("#nonpay").show();
    return false;
  });

  $(".closebtn_btn").click(function () {
    $(".popup-wrapper").hide();
    return false;
  });

  $(".xIcon").click(function () {
    $(".sidebar").animate({ top: "-100vh" }, 800, function () {
      $(".sidebar").css({ display: "none" });
    });
    return false;
  });

  $(document).on("input propertychange", ".number_only", function (e) {
    $(this).val(
      $(this)
        .val()
        .replace(/[^0-9]/g, "")
    );
  });
});

$(document).click(function (e) {
  let LayerPopup = $(".cont");
  if (LayerPopup.has(e.target).length === 0) {
    $(".popup-wrapper").css("display", "none");
  }
});
