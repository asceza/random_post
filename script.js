const buttonHabr = document.getElementById('btn_habr');

// Добавим обработчик для события "click", предоставив callback.
// Теперь по клику на элемент будет всплывать подсказка.

buttonHabr.addEventListener('click', function (event) {
  // alert('Событие вызвано функцией!');

  const contentHabr = document.getElementById('content_habr');
  contentHabr.innerHTML = 'Замена текущего текста';
});
