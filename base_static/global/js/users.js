(async function() {
    console.clear();
    const headers = {
        authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0MjkwNjU1LCJpYXQiOjE2NjQyODcwNTUsImp0aSI6ImQ3MTI2OWE5ZTMxMTQ0ZWM5YWNmOTg1NDg0NTgxODA1IiwidXNlcl9pZCI6MX0.07DrghXdG4Ypj7SMJ8kS-_21PZjQK_KZiuYTqethS3w',
    };
    const config = {
        method: 'GET',
        headers: headers,
    };
    const response = await fetch(
        'http://localhost:8000/api/maintenance/',
        config
    );
    const json = await response.json();

    console.log('STATUS', response.status);
    console.log(json);
})();