const themeSwitch = document.getElementById('theme-switch');

themeSwitch.addEventListener('change',()=>{
    localStorage.setItem('mode', JSON.stringify(themeSwitch.value));
});

if(localStorage.getItem('mode')){
    themeSwitch.checked=(JSON.parse(localStorage.getItem('mode')).includes('dark'));
}