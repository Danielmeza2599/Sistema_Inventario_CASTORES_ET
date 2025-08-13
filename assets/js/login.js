document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorElement = document.getElementById('error-message');
    errorElement.style.display = 'none';
    
    try {
        const response = await fetch('http://localhost:5500/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || `Error HTTP: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success) {
            // Redirigir al dashboard
            window.location.href = '/dashboard';
        } else {
            throw new Error(data.message || 'Credenciales incorrectas');
        }
    } catch (error) {
        console.error('Error en el login:', error);
        errorElement.textContent = error.message;
        errorElement.style.display = 'block';
    }
});