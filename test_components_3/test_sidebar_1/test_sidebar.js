window.addEventListener('resize', function() {
    const menuActive = document.getElementById('menu_active');
    if (window.innerWidth < 600) {
        menuActive.checked = true; // Check the box if the viewport is smaller than 600px
    }
    else{
        menuActive.checked=false;
    }
});