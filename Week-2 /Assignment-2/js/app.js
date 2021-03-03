// Request 1: Click to Change Text.
const wm = document.getElementById('wm');

wm.addEventListener('click', ()=>
{document.querySelector('header').innerHTML = "<h1>Have a Good Time!</h1>"
});

//Request 2: Click to Show More Content Boxes.
const ctc = document .getElementById('ctc');

bx1 = document.querySelector('.show1');
bx1.style.display="none";

bx2 = document.querySelector('.show2');
bx2.style.display="none";

bx3 = document.querySelector('.show3');
bx3.style.display="none";

bx4 = document.querySelector('.show4');
bx4.style.display="none";

ctc.addEventListener('click', ()=>
{if (document.querySelector('.show1').style.display =="inline-block") {
  bx1.style.display="none";
  bx2.style.display="none";
  bx3.style.display="none";
  bx4.style.display="none";
} else {
  bx1.style.display="inline-block";
  bx2.style.display="inline-block";
  bx3.style.display="inline-block";
  bx4.style.display="inline-block";
}
});
