// https://learn.javascript.ru/fetch

function funonload() {
  fetch('http://127.0.0.1:5000/vc')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentVC = document.getElementById('content_vc');
      contentVC.innerHTML = data;
    });

  fetch('http://127.0.0.1:5000/dtf')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentDTF = document.getElementById('content_dtf');
      contentDTF.innerHTML = data;
    });

  fetch('http://127.0.0.1:5000/tjournal')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contenttjournal = document.getElementById('content_tjournal');
      contenttjournal.innerHTML = data;
    })
}

window.onload = funonload;



// VC
const buttonVC = document.getElementById('btn_vc');
// Добавим обработчик для события "click", предоставив callback.
// Теперь по клику на элемент будет всплывать подсказка.
buttonVC.addEventListener('click', function(event) {
  fetch('http://127.0.0.1:5000/vc')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentVC = document.getElementById('content_vc');
      contentVC.innerHTML = data;
    })
});


// DTF
const buttonDTF = document.getElementById('btn_dtf');
buttonDTF.addEventListener('click', function(event) {
  fetch('http://127.0.0.1:5000/dtf')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentDTF = document.getElementById('content_dtf');
      contentDTF.innerHTML = data;
    })
});


// tjournal
const buttontjournal = document.getElementById('btn_tjournal');
buttontjournal.addEventListener('click', function(event) {
  fetch('http://127.0.0.1:5000/tjournal')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contenttjournal = document.getElementById('content_tjournal');
      contenttjournal.innerHTML = data;
    })
});
