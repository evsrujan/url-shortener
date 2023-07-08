var preload = document.getElementById('loading')
    function myfun(){
        preload.style.display = 'none';
    }
let copyText = document.querySelector(".data");
copyText.querySelector("button").addEventListener("click",function(){
    let input = copyText.querySelector("#value");
    input.select();
    document.execCommand('copy');
    copyText.classList.add("active");
    window.getSelection().removeAllRanges();
    setTimeout(function(){
        copyText.classList.remove("active");
    },2500);
});

