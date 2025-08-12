// javascript
// filepath: c:\Users\danie\Documents\Software_Development\CASTORES\Desarrollo\Sistema_Inventario_CASTORES_ET\assets\js\login.js
// ...existing code...
// Simple frontend validation (replace with backend logic in production)
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Example: hardcoded credentials
    if(username === 'admin' && password === 'admin123') {
        window.location.href = 'dashboard.html'; // Redirect to dashboard
    } else {