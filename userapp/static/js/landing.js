$(document).ready(function () {
    $('#submit').click(function () {
        $.scrollTo($('#results'), 500);
    });

    $('.book').click(function () {
        $(this).toggleClass("book");
    });
})