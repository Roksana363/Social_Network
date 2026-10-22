const themeSelect = document.getElementById('theme-select');

themeSelect.value = localStorage.getItem('theme') || 'light';

document.documentElement.setAttribute('data-theme', themeSelect.value);

themeSelect.addEventListener('change', function() {
    document.documentElement.setAttribute('data-theme', this.value);
    localStorage.setItem('theme', this.value);
});