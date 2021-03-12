const addNameButton = document.querySelector('button.addNameButton');
const addNameInput = document.querySelector('input.addNameInput');

addNameButton.addEventListener('click', () => {
  let ul = document.getElementsByTagName('ul')[0];
  let li = document.createElement('li');
  li.textContent = addNameInput.value;
  ul.appendChild(p);
  addNameInput.value = '';
});