
document.addEventListener("DOMContentLoaded", function() {
      var navToggle = document.getElementById("nav-toggle");
      
  
 
  
  var navLinks = document.querySelectorAll("#nav-content a"); // ID'si doğru mu?
  
  // Nav linklerine tıklama olayı
  navLinks.forEach(function(link) {
      link.addEventListener("click", function() {
          navToggle.checked = false; // Checkbox'u kaldır
          content.style.filter = "none"; // Filtreyi temizle
      });
  });

  

window.addEventListener('resize', function() {
  var navToggle = document.getElementById("nav-toggle");
  var navBar = document.getElementById("nav-bar"); // ID'si doğru mu?
  var screenWidth = window.innerWidth;

  if (!navToggle || !navBar) {
      console.error("Nav-toggle veya nav-bar elemanı bulunamadı.");
      return;
  }
  var content = document.getElementById("content");
  var header=document.getElementById("demo-header");
  if (screenWidth <= 1100 &&navToggle.checked==false) {
    navToggle.checked = true;
    navBar.style.backgroundColor = "";
    content.style.filter = "none"; 
    header.style.filter="none";
     
  } else {
      navToggle.checked = false;
      
      navToggle.addEventListener("click", function() {
      
      if (navToggle.checked!=false && screenWidth) {
        navBar.style.backgroundColor = "";
        content.style.filter = "none"; 
        header.style.filter="none";
      }
      else{
        navBar.style.backgroundColor = "rgba(0,0,0,0.65)";
        content.style.filter = "blur(5px)"; 
        header.style.filter="blur(5px)";
        
      }
      })
  }
})
window.addEventListener("resize", function() {
  var screenWidth = window.innerWidth;
  var navToggle = document.getElementById("nav-toggle");
  if (screenWidth > 1100) {
      console.log("test",navToggle);
      navToggle.checked = false;
      content.style.filter = "none"; 
      header.style.filter="none";
  }
});
});


