(async function() {
    console.clear();
    const headers = {
        'Content-Type': 'application/json',
    };
    const init = JSON.stringify({
        "username": "admin",
        "password": "admin"
    });
    const config = {
        method: 'POST',
        headers: headers,
        body: init 
    };
    const response = await fetch(
        'http://localhost:8000/api/api/token/',
        config
    );
    const json = await response.json();

    console.log('STATUS', response.status);
    console.log(json.access);
})();