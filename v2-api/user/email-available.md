# email-available

## API Example

{% swagger method="get" path="/email-available" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to check avaliablity of a username on registration & username changes.
{% endswagger-description %}

{% swagger-parameter in="path" name="username" type="String" required="true" %}

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

| bad\_ref\_id | reason                   |
| ------------ | ------------------------ |
| 1            | Invalid email.           |
| 2            | Email taken              |
| 3            | Email domain blacklisted |
