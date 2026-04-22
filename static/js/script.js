document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Get inputs
    const area = document.getElementById('area').value;
    const bedrooms = document.getElementById('bedrooms').value;
    const age = document.getElementById('age').value;
    
    // UI Elements
    const btnText = document.querySelector('.btn-text');
    const loader = document.getElementById('loader');
    const resultContainer = document.getElementById('result-container');
    const priceResult = document.getElementById('price-result');
    const errorMessage = document.getElementById('error-message');
    
    // Set loading state
    btnText.style.display = 'none';
    loader.style.display = 'block';
    
    // Hide previous results
    resultContainer.classList.add('hidden');
    errorMessage.classList.add('hidden');
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ area, bedrooms, age }),
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Success
            // Format number as currency
            const formatter = new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: 'USD',
                maximumFractionDigits: 0,
            });
            
            priceResult.textContent = formatter.format(data.price);
            priceResult.style.color = '#34d399'; // reset color if it was error
            errorMessage.classList.add('hidden');
            
            // Show result with animation
            setTimeout(() => {
                resultContainer.classList.remove('hidden');
            }, 100);
            
        } else {
            // API Error
            priceResult.textContent = 'Error';
            priceResult.style.color = '#f87171';
            errorMessage.textContent = data.error || 'Something went wrong';
            errorMessage.classList.remove('hidden');
            resultContainer.classList.remove('hidden');
        }
    } catch (err) {
        // Network Error
        priceResult.textContent = 'Error';
        priceResult.style.color = '#f87171';
        errorMessage.textContent = 'Failed to connect to the server.';
        errorMessage.classList.remove('hidden');
        resultContainer.classList.remove('hidden');
    } finally {
        // Reset loading state
        btnText.style.display = 'block';
        loader.style.display = 'none';
    }
});
