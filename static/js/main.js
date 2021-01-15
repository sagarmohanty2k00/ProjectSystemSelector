let r = 0;

function selectSystem(){
    r = r + 1;
    if(r > 1){
        textToDelete = document.getElementById(r-1);
        textToDelete.classList.add('d-none');
    }
    wait = document.getElementById('fade');
    wait.classList.remove('d-none');
    fadeout();
    setTimeout(function(){
        wait.classList.add('d-none');
        text = document.getElementById(r);
        text.classList.remove('d-none')
        textId = document.getElementsByName(r);
        input = document.getElementById('systemInput');
        input.value = textId.innerHTML;
    }, 5000)

    assign = document.getElementById('assign');
    assign.classList.remove('d-none');
}

    function fadeout(){
        setTimeout(function() {
    var fade = document.getElementById("fade");
    fade.style.opacity = 1;
    var timerId = setInterval(function() {
        var opacity = fade.style.opacity;
        if (opacity == 0) {
        clearInterval(timerId);
        } else {
        fade.style.opacity = opacity - 0.01;
        }
    }, 50);
    },1000);
}