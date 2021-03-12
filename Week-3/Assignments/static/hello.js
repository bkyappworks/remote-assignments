function sayHello() {
    alert("Hello World")
 }
function loadDoc() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    document.getElementById("demo").innerHTML = this.responseText;
    }
};
xhttp.open("GET", "ajax_info.txt", true);
xhttp.send();
}


function aaa() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    document.getElementById("demo").innerHTML = this.responseText;
    }
};
xhttp.open("POST", "ajax_info.txt", true);
xhttp.send();
}

const addNameButton = document.querySelector('button.addNameButton');
const addNameInput = document.querySelector('input.addNameInput');

addNameButton.addEventListener('click', () => {
    let ul = document.getElementsByTagName('ul')[0];
    let li = document.createElement('li');
    li.textContent = addNameInput.value;
    ul.appendChild(p);
    addNameInput.value = '';
  });