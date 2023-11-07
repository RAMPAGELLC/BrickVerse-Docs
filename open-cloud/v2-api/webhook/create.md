# create

{% swagger method="post" path="/create" baseUrl="https://api.brickverse.co/v2/webhook" summary="Information" %}
{% swagger-description %}
API used to create webhooks.
{% endswagger-description %}

{% swagger-parameter in="body" name="URL" type="String" required="true" %}
Ensure you have a Port defined for IPv4's if required. (Example: 127.0.0.1:3000)
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
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
