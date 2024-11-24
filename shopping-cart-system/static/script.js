async function fetchCart() {
    const response = await fetch('/cart');
    const cart = await response.json();
    updateCartUI(cart);
}

async function addToCart(name, price) {
    await fetch('/cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, price })
    });
    fetchCart();
}

async function updateCart(name, quantity) {
    await fetch('/cart', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, quantity })
    });
    fetchCart();
}

async function removeFromCart(name) {
    await fetch('/cart', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    });
    fetchCart();
}

function updateCartUI(cart) {
    const cartItemsContainer = document.getElementById('cart-items');
    const totalContainer = document.getElementById('total');
    cartItemsContainer.innerHTML = '';

    let total = 0;
    cart.forEach(item => {
        total += item.price * item.quantity;
        cartItemsContainer.innerHTML += `
            <tr>
                <td>${item.name}</td>
                <td>$${item.price}</td>
                <td>
                    <input type="number" value="${item.quantity}" min="1" onchange="updateCart('${item.name}', parseInt(this.value))">
                </td>
                <td>
                    <button onclick="removeFromCart('${item.name}')">Remove</button>
                </td>
            </tr>
        `;
    });

    totalContainer.textContent = `Total: $${total.toFixed(2)}`;
}

document.addEventListener('DOMContentLoaded', fetchCart);
