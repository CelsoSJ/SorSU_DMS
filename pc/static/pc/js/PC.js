const body=document.querySelector('body'),
      sidebar=body.querySelector('.sidebar'),
     
     
      bodyClick=body.querySelector('main');




bodyClick.addEventListener('click',()=>{
  sidebar.classList.remove('open');
})

document.addEventListener('DOMContentLoaded',function() {
  const toggleButton=body.querySelector('.switch-container');
  const currentTheme=localStorage.getItem('theme');

  if (currentTheme){
    body.classList.add(currentTheme);
  }

  toggleButton.addEventListener('click',function() {
    body.classList.toggle('dark');
    
    let theme='light';
    if(body.classList.contains('dark')){
      theme = 'dark';
    }

    localStorage.setItem('theme',theme);
  });
}
);


document.addEventListener('DOMContentLoaded',function() {
  const sidebarToggle=body.querySelector('.sidebar-toogle');
  const currentSidebar=localStorage.getItem('sidebar');
  const Sidebar=body.querySelector('.sidebar')

  if (currentSidebar){
    Sidebar.classList.add(currentSidebar);
  }

  sidebarToggle.addEventListener('click',function() {
    Sidebar.classList.toggle('open');
    
    let sidebar='close';
    if(Sidebar.classList.contains('open')){
      sidebar = 'open';
    }

    localStorage.setItem('sidebar',sidebar);
  });
}
);



//This is for Create_Submission
var modal = document.getElementById("myModal");

var btn = document.getElementById("myBtn");

var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


//This is for My_Profile
document.getElementById("btn1").addEventListener("click", function() {
  document.getElementById("content1").style.display = "block";
  document.getElementById("content2").style.display = "none";
});

document.getElementById("btn2").addEventListener("click", function() {
  document.getElementById("content1").style.display = "none";
  document.getElementById("content2").style.display = "block";
});
