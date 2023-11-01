# bot-login



{% swagger method="post" path="/bot-login" baseUrl="https://api.brickverse.co/v2/auth" summary="Information" expanded="false" %}
{% swagger-description %}
API used to log into accounts.
{% endswagger-description %}

{% swagger-parameter in="body" name="bot_token" required="true" type="String" %}

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
