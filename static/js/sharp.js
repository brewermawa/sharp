categoryMenu = document.querySelector("#category-menu")
categoryDropDown = document.querySelector("#category-dropdown")
hamburguer = document.querySelector("#hamburguer-icon")
hamburguerMenu = document.querySelector("#hamburguer-menu")
closeHamburguerMenu = document.querySelector("#close-hamburguer-menu")
info = document.querySelectorAll(".info-title")
tabs = document.querySelectorAll(".tab")
tabsContent = document.querySelectorAll(".tab-content")


categoryMenu.addEventListener("click", () => {
    categoryDropDown.classList.toggle("grow-down");
    categoryDropDown.classList.toggle("show");

    document.getElementById("chevron-down-cat").classList.toggle("hide");
    document.getElementById("chevron-up-cat").classList.toggle("show");
})

window.onclick = function(event) {
    if (!(event.target.id === "menu-title" || event.target.parentElement.id === "menu-title" )) {
        if(categoryDropDown.classList.contains("show")) {
            categoryDropDown.classList.toggle("grow-down");
            categoryDropDown.classList.remove("show");

            document.getElementById("chevron-down-cat").classList.toggle("hide");
            document.getElementById("chevron-up-cat").classList.toggle("show");
        }
    }
}

hamburguer.addEventListener("click", () => {
    hamburguerMenu.classList.add("show");
    closeHamburguerMenu.classList.add("show-hamburguer-close");
})

closeHamburguerMenu.addEventListener("click", () => {
    hamburguerMenu.classList.remove("show");
    closeHamburguerMenu.classList.remove("show-hamburguer-close");
})

info.forEach(infoSection => {
    infoSection.addEventListener("click", () => {
        id = infoSection.id[5];
        infoLink = document.getElementById("info-links-" + id)
        infoLink.classList.toggle("show");

        document.getElementById("chevron-down-" + id).classList.toggle("hide");
        document.getElementById("chevron-up-" + id).classList.toggle("show");
    })
});

tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        tabs.forEach(t => t.classList.remove("tab-selected"));
        tab.classList.add("tab-selected");
        id = tab.id[4];
        
        tabsContent.forEach(tc => tc.classList.add("hide"));
        document.getElementById("tab-content-" + id).classList.remove("hide");
        document.getElementById("tab-content-" + id).classList.add("show");
    });
});

var slideIndex = 0;
var slides = document.getElementsByClassName("slide");
var dots = document.getElementsByClassName("slider-dot")
carousel();

for (x = 1; x <= dots.length; x++) {
    document.getElementById("dot-"+x).addEventListener("click", (e) => {
        selectSlide(parseInt(e.target.id.substring(4)));
    })
}

function selectSlide(slideNum) {
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideNum-1].style.display = "block";
    slideIndex = slideNum;

    for (dot=0; dot < dots.length; dot++) {
        if (dot === slideNum-1) {
            dots[dot].classList.remove("mdi-circle-outline")
            dots[dot].classList.add("mdi-circle")
        }
        else {
            dots[dot].classList.remove("mdi-circle")
            dots[dot].classList.add("mdi-circle-outline")
        }
    }
}

function carousel() {
    var i;

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1
    }

    selectSlide(slideIndex);

    setTimeout(carousel, 30000);
}
