//seach-button
const search = document.querySelector('.search-button');
const bar = document.querySelector('.search-bar');
const btn = document.querySelector('.search-btn');


function activate() {
    search.classList.toggle('active-search');
    bar.value = '';
    setTimeout(() => bar.focus(), 750)
}

btn.addEventListener('click', activate, false);

//moon-sun mode
let moon = document.getElementById('moon')
let sun = document.getElementById('sun')

document.addEventListener("DOMContentLoaded", function () {
    const darkMode = localStorage.getItem("darkMode") === "true";
    document.body.classList.toggle("dark-mode", darkMode);
});

// Toggle butonuna tıklanınca dark-mode durumunu değiştir ve localStorage'a kaydet
document.querySelector(".moon-sun-button").addEventListener("click", () => {
    const body = document.body;
    const darkMode = body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", darkMode);
    moon.classList.toggle('d-none')
    sun.classList.toggle('d-none')
});
