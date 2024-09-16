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