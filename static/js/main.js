document.addEventListener("DOMContentLoaded", () => {
    const burger = document.getElementById("burger");
    const menu = document.getElementById("mobileMenu");

    if (burger && menu) {
        burger.addEventListener("click", () => {
            menu.classList.toggle("active");
        });
    }
});
