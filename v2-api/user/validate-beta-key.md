# validate-beta-key

## API Example

{% swagger method="get" path="/validate-beta-key" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to check if a beta  key is valid or not for registration.
{% endswagger-description %}

{% swagger-parameter in="path" name="beta-key" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "valid": boolean}
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

| bad\_ref\_id | reason      |
| ------------ | ----------- |
| 1            | Invalid key |
