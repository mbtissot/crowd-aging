const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;
const darkModeIcon = document.getElementById('darkModeIcon');

const exampleImageSuc = document.getElementById('exampleImageSuc');
const exampleImageFail = document.getElementById('exampleImageFail');

if (localStorage.getItem('theme') === 'dark') {
  body.classList.add('dark-mode');
  darkModeIcon.src = "/static/imgs/light-mode-icon.png";  // Set the image to dark mode
  darkModeIcon.title = "Modo Claro";
  darkModeIcon.alt = "Modo Claro";
  if (exampleImageSuc && exampleImageFail) {
    console.log("1");
    exampleImageSuc.src = "/static/imgs/exemplo_escuro_suc.png";
    exampleImageFail.src = "/static/imgs/exemplo_escuro_falha.png";
  }
} else {
  body.classList.remove('dark-mode');
  darkModeIcon.src = "/static/imgs/dark-mode-icon.png";  // Set the image to light mode
  darkModeIcon.title = "Modo Escuro";
  darkModeIcon.alt = "Modo Escuro";
  if (exampleImageSuc && exampleImageFail) {
    exampleImageSuc.src = "/static/imgs/exemplo_claro_suc.png";
    exampleImageFail.src = "/static/imgs/exemplo_claro_falha.png";
    console.log("2");
  }
}

darkModeToggle.addEventListener("click", function() {
  body.classList.toggle("dark-mode");

  console.log("Changed mode");
  
  // Toggle button image
  if (body.classList.contains("dark-mode")) {
    darkModeIcon.src = "/static/imgs/light-mode-icon.png";
    darkModeIcon.title = "Modo Claro";
    darkModeIcon.alt = "Modo Claro";
    if (exampleImageSuc && exampleImageFail) {
        exampleImageSuc.src = "/static/imgs/exemplo_escuro_suc.png";
        exampleImageFail.src = "/static/imgs/exemplo_escuro_falha.png";
        console.log("3");
    }
    localStorage.setItem('theme', 'dark');  // Save the dark mode preference
  } else {
    darkModeIcon.src = "/static/imgs/dark-mode-icon.png";
    darkModeIcon.title = "Modo Escuro";
    darkModeIcon.alt = "Modo Escuro";
    if (exampleImageSuc && exampleImageFail) {
        exampleImageSuc.src = "/static/imgs/exemplo_claro_suc.png";
        exampleImageFail.src = "/static/imgs/exemplo_claro_falha.png";
        console.log("4");
    }
    localStorage.setItem('theme', 'light');  // Save the light mode preference
  }
});