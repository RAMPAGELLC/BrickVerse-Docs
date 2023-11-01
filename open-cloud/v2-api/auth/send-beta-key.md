# send-beta-key

{% swagger method="post" path="/send-beta-key/{email}" baseUrl="https://api.brickverse.co/v2/auth" summary="Information" expanded="false" %}
{% swagger-description %}
Forward your beta key to your e-mail address.

Account registered with the e-mail is required.
{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "success": true,
    "message": ...
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{"status": "error", "message": ...}
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
