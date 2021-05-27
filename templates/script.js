$(document).ready(function () {
    $("input:checkbox").click(function () {
        $("[name="+$(this).prop('name')+"]").prop("checked", false);
        $(this).prop("checked", true);
    });
});

function infoCam() {
    var popup1 = document.getElementById("info");
    var popup2 = document.getElementById("info2");
    var popup3 = document.getElementById("info3");
    var popup4 = document.getElementById("info4");
    popup1.classList.toggle("show");
    popup2.classList.toggle("show");
    popup4.classList.toggle("show");
    popup3.classList.toggle("show");
}

function infoFly() {
    var popup1 = document.getElementById("infoP");
    var popup2 = document.getElementById("infoP1");
    var popup3 = document.getElementById("infoP2");
    var popup4 = document.getElementById("infoP3");
    popup1.classList.toggle("show");
    popup2.classList.toggle("show");
    popup3.classList.toggle("show");
    popup4.classList.toggle("show");
}