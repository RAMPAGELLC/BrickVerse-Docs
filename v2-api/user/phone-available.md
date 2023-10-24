# phone-available

## API Example

{% swagger method="get" path="/phone-available/{number}" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to check if a phone number is available for linking.
{% endswagger-description %}

{% swagger-parameter in="path" name="number" type="Int" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="ignore_history" type="Bool" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "available": boolean}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="" %}
```json
{"status": "error"}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}

## Bad Reference ID (bad\_ref\_id)

| bad\_ref\_id | reason             |
| ------------ | ------------------ |
| 1            | Invalid Number.    |
| 2            | Number taken       |
| 3            | Number blacklisted |
