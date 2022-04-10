// Вы зашли сюда скорее всего чтобы изучить мой JS код.
// Но вся логика написана на беке.
// Лучше пишите мне в телегу https://t.me/wezochy

function funonload() {
  fetch('https://wezochy-random-post.herokuapp.com/vc')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentVC = document.getElementById('content_vc');
      contentVC.innerHTML = data;
    });

  fetch('https://wezochy-random-post.herokuapp.com/dtf')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentDTF = document.getElementById('content_dtf');
      contentDTF.innerHTML = data;
    });

  fetch('https://wezochy-random-post.herokuapp.com/tjournal')
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
  fetch('https://wezochy-random-post.herokuapp.com/vc')
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
  fetch('https://wezochy-random-post.herokuapp.com/dtf')
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
  fetch('https://wezochy-random-post.herokuapp.com/tjournal')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contenttjournal = document.getElementById('content_tjournal');
      contenttjournal.innerHTML = data;
    })
});
