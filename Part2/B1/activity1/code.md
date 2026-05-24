// ❌ BAD: The API key is hardcoded directly into the source code
const apiKey = "sk_live_51Nx...THIS_IS_A_SECRET_KEY...9zL2"; 
const apiURL = "https://api.paymentprovider.com/v1/charges";

async function processPayment(amount) {
    const response = await fetch(apiURL, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amount })
    });
    return response.json();
}
