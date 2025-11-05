// RKL Dashboard JavaScript

// Filter tasks by status
function filterTasks(status) {
    const tasks = document.querySelectorAll('.task-item');
    const buttons = document.querySelectorAll('.filter-btn');

    // Update active button
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Show/hide tasks
    tasks.forEach(task => {
        if (status === 'all') {
            task.style.display = 'flex';
        } else {
            if (task.dataset.status === status) {
                task.style.display = 'flex';
            } else {
                task.style.display = 'none';
            }
        }
    });
}

// Quick action buttons
async function quickAction(action) {
    const response = await fetch(`/quick_action/${action}`);
    const data = await response.json();

    showNotification(data.message, data.status);

    // If previewing website, open in new tab after a second
    if (action === 'preview_website' && data.status === 'ok') {
        setTimeout(() => {
            window.open('http://localhost:1313', '_blank');
        }, 2000);
    }
}

// Refresh meeting packet status
async function refreshPacket() {
    showNotification('Refreshing meeting packet status...', 'info');

    const response = await fetch('/api/refresh_packet');
    const data = await response.json();

    if (data.status === 'ok') {
        showNotification('Meeting packet status refreshed!', 'ok');
        // Reload page to show updated status
        setTimeout(() => location.reload(), 1000);
    } else {
        showNotification('Error refreshing packet: ' + data.message, 'error');
    }
}

// Show notification
function showNotification(message, status) {
    // Remove existing notifications
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }

    // Create notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${status}`;
    notification.textContent = message;

    // Style notification
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 1000;
        animation: slideIn 0.3s ease;
        max-width: 400px;
    `;

    if (status === 'ok') {
        notification.style.background = '#10b981';
        notification.style.color = 'white';
    } else if (status === 'error') {
        notification.style.background = '#ef4444';
        notification.style.color = 'white';
    } else {
        notification.style.background = '#0F4C81';
        notification.style.color = 'white';
    }

    document.body.appendChild(notification);

    // Auto-remove after 5 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

// Add CSS animation for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Handle file link clicks
document.addEventListener('click', async (e) => {
    if (e.target.closest('.file-link')) {
        e.preventDefault();
        const link = e.target.closest('.file-link');
        const href = link.getAttribute('href');

        const response = await fetch(href);
        const data = await response.json();

        showNotification(data.message, data.status);
    }

    // Handle Open buttons in file list
    if (e.target.classList.contains('btn-tiny')) {
        e.preventDefault();
        const href = e.target.getAttribute('href');

        const response = await fetch(href);
        const data = await response.json();

        showNotification(data.message, data.status);
    }
});

// Auto-refresh status every 5 minutes
setInterval(async () => {
    const response = await fetch('/api/status');
    const data = await response.json();

    // Update percentage in header
    const percentageEl = document.querySelector('.stat-value');
    if (percentageEl && data.summary) {
        percentageEl.textContent = data.summary.percentage + '%';
    }

    console.log('Status refreshed:', data);
}, 300000); // 5 minutes

// Welcome message on load
window.addEventListener('load', () => {
    showNotification('Welcome to RKL Dashboard! 🚀', 'ok');
});
