document.addEventListener('DOMContentLoaded', function() {
    // Mostrar el nombre de usuario
    fetch('/get-user')
        .then(response => response.json())
        .then(data => {
            if(data.username) {
                document.getElementById('username-display').textContent = data.username;
            }
        });
    
    // Cargar datos del dashboard
    loadDashboardData();
    
    // Configurar gráfico
    setupChart();
});

function loadDashboardData() {
    fetch('/api/dashboard-data')
        .then(response => response.json())
        .then(data => {
            // Actualizar widgets
            document.getElementById('total-products').textContent = data.totalProducts;
            document.getElementById('low-stock').textContent = data.lowStockItems;
            document.getElementById('total-warehouses').textContent = data.totalWarehouses;
            
            // Llenar tabla de stock bajo
            const tableBody = document.querySelector('#low-stock-table tbody');
            tableBody.innerHTML = '';
            
            data.lowStockProducts.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.code}</td>
                    <td>${product.name}</td>
                    <td>${product.warehouse}</td>
                    <td class="${product.currentStock < product.minStock ? 'text-danger' : ''}">
                        ${product.currentStock}
                    </td>
                    <td>${product.minStock}</td>
                    <td>
                        <button class="btn btn-sm">Reabastecer</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        });
}

function setupChart() {
    const ctx = document.getElementById('movements-chart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            datasets: [{
                label: 'Entradas',
                data: [12, 19, 3, 5, 2, 3],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                tension: 0.1
            }, {
                label: 'Salidas',
                data: [8, 15, 5, 8, 3, 6],
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                }
            }
        }
    });
}