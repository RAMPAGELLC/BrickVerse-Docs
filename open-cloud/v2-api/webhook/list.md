# list

{% swagger method="post" path="/list" baseUrl="https://api.brickverse.co/v2/webhook" summary="Information" %}
{% swagger-description %}
API used to list webhooks you have created.
{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "list": [
        {
            "id": 1,
            "ownerid": 1,
            "url": "https://127.0.0.1",
            "created": 000000000
        }
    ]
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{
    "status": "error",
    "message": "Invalid request, missing some post fields.",
    "got": null
}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="" %}
```json
{"status": "error", "message": 403}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}
