# delete

{% swagger method="delete" path="/delete/{id}" baseUrl="https://api.brickverse.co/v2/cloud/bricklinks" summary="Information" %}
{% swagger-description %}
API used to delete a specific brick link.
{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok"
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
