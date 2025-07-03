console.log('coucou');
const gsmarenaUrlInput = document.getElementById('id_gsmarena_url');
gsmarenaUrlInput.classList.add('col2');
const gsmarenaButton = document.createElement('button');
gsmarenaButton.classList = "button";
gsmarenaButton.textContent = "Remplir avec gsmarena";
gsmarenaUrlInput.parentElement.classList.add('w-field-row');
gsmarenaUrlInput.parentElement.appendChild(gsmarenaButton);

gsmarenaButton.addEventListener('click', (e)=>{
  e.preventDefault();
  fetch('/phone/get-gsmarena-data/?url=' + gsmarenaUrlInput.value)
    .then( (response) => response.json())
    .then((data) => {
    console.log(data);
    for (let [field, spec] of Object.entries(data)) {
      let input = document.getElementById(`id_${field}`);
      if (input){input.value = spec};
    }
    gsmarenaButton.disabled = true;
    setTimeout(()=>{gsmarenaButton.disabled = false;},5000);
  });
});