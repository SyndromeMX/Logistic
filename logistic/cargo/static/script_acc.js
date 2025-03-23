function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
}

document.addEventListener('click', function (event) {
    const sidebar = document.querySelector('.sidebar');
    const toggleBtn = document.querySelector('.toggle-btn');

    if (!sidebar.contains(event.target) && !toggleBtn.contains(event.target)) {
        sidebar.classList.remove('active');
    }
});

function enableEditMode() {
    document.querySelector('.info-card').style.display = 'none';
    document.getElementById('edit-button').style.display = 'none';

    document.getElementById('edit-form').style.display = 'block';
}

function disableEditMode() {
    document.querySelector('.info-card').style.display = 'block';
    document.getElementById('edit-button').style.display = 'block';

    document.getElementById('edit-form').style.display = 'none';
}