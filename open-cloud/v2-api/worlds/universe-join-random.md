# /{universe}/join/random

{% swagger method="get" path="/join/random" baseUrl="https://api.brickverse.co/v2/worlds/{universe_id}" summary="Information" expanded="false" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="query" name="launch_client" type="Bool" %}
Launch brickverse client or not.
{% endswagger-parameter %}

{% swagger-parameter in="query" name="return_url" type="String" %}
Redirect a user after launching the client. launch\_client query param is required.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "success": true, "client_join_token": "XXXXXXXXXXXXXXX"}
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
