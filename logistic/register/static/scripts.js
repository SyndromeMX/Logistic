
// Обработка формы входа
document.getElementById('login-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Вы успешно вошли в систему!');
    // Здесь можно добавить код для отправки данных на сервер
});

// Обработка формы регистрации
document.getElementById('register-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Регистрация прошла успешно!');
    // Здесь можно добавить код для отправки данных на сервер
});