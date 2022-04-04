const buttonVC = document.getElementById('btn_vc');

// Добавим обработчик для события "click", предоставив callback.
// Теперь по клику на элемент будет всплывать подсказка.

buttonVC.addEventListener('click', function(event) {
  // alert('Событие вызвано функцией!');

  fetch('http://127.0.0.1:5000/vc')
    .then(data => {
      return data.text();
    })
    .then(data => {
      const contentVC = document.getElementById('content_vc');
      contentVC.innerHTML = data;
    })

  // fetch('http://127.0.0.1:5000/')
  //   .then(data => {
  //     const contentVC = document.getElementById('content_vc');
  //     contentVC.innerHTML = data;
  //   })

});
