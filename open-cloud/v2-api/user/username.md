# username

## API Example

{% swagger method="get" path="/username" baseUrl="https://api.brickverse.co/v2/user" summary="Information" expanded="true" %}
{% swagger-description %}
API used to pull limited amount of user-data.
{% endswagger-description %}

{% swagger-parameter in="path" name="username" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "found": boolean}
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

{% hint style="info" %}
Example JSON Response: [https://api.brickverse.co/v2/user/id/1](https://api.brickverse.co/v2/user/id/1)
{% endhint %}
