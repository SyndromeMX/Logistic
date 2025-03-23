document.getElementById('login-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Вы успешно вошли в систему!');
});

document.getElementById('register-form')?.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Регистрация прошла успешно!');
});