const pagarButton = document.getElementById('pagar-button');

pagarButton.addEventListener('click', () => {
    const producto = 'Producto de prueba';
    const precio = '100.00';
    fetch('/pagar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ producto, precio })
    })
    .then(response => response.text())
    .then(url => window.location.href = url);
});