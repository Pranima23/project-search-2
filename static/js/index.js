
const translate = document.querySelectorAll(".translate");
const big_title = document.querySelector(".big-title");
const header = document.querySelector("header");
const shadow = document.querySelector(".shadow");
const content = document.querySelector(".content");
const section = document.querySelector("section");
const image_container = document.querySelector(".imgContainer");
const opacity = document.querySelectorAll(".opacity");
const border = document.querySelector(".border");

let header_height = header.offsetHeight;
let section_height = section.offsetHeight;

window.addEventListener('scroll', () => {
    let scroll = window.pageYOffset;
    let sectionY = section.getBoundingClientRect();
    
    translate.forEach(element => {
        let speed = element.dataset.speed;
        element.style.transform = `translateY(${scroll * speed}px)`;
    });

    opacity.forEach(element => {
        element.style.opacity = scroll / (sectionY.top + section_height);
    })

    big_title.style.opacity = - scroll / (header_height / 2) + 1;
    shadow.style.height = `${scroll * 0.5 + 300}px`;

    content.style.transform = `translateY(${scroll / (section_height + sectionY.top) * 50 - 50}px)`;
    image_container.style.transform = `translateY(${scroll / (section_height + sectionY.top) * -50 + 50}px)`;

    border.style.width = `${scroll / (sectionY.top + section_height) * 30}%`;
})

/*

document.getElementById("button").addEventListener("click",
function(){
    document.querySelector(".popup").style.display ="flex";
})

document.getElementById("button1").addEventListener("click",
function(){
    document.querySelector(".popup1").style.display ="flex";
})

document.querySelector(".empty").addEventListener("click",
function(){
    document.querySelector(".popup").style.display ="none";
})

document.querySelector(".emptys").addEventListener("click",
function(){
    document.querySelector(".popup1").style.display ="none";
})

*/

function Appear(){
    var message= document.getElementById("button3");
    window.alert("You Must Login First!");
 }
 
 function Wel()
 {
     var We= document.getElementById("WEL");
     window.alert("Congratulations! Welcoming you to the Home Site!");
 }
