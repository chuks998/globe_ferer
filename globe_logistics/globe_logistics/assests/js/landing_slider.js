document.addEventListener("DOMContentLoaded", function () {
    const landing = document.getElementById("landingPage");
    const images = [
        landing.dataset.bg1,
        landing.dataset.bg2,
        landing.dataset.bg3
    ];
    let idx = 0;

    function setBg() {
        landing.style.backgroundImage = `url('${images[idx]}')`;
    }

    setBg();
    setInterval(() => {
        idx = (idx + 1) % images.length;
        setBg();
    }, 4000); // Change every 4 seconds
});
