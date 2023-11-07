# send

{% swagger method="post" path="/feed/send" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API to send to your user feed.
{% endswagger-description %}

{% swagger-parameter in="body" name="content" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "success": true}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{"status": "error", "message": "reason_string"}
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
