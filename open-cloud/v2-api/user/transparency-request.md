# transparency-request

{% hint style="warning" %}
Account authentication required. Read about account authentication at [https://developers.brickverse.co/v2-api/auth/bot-login](https://developers.brickverse.co/v2-api/auth/bot-login).
{% endhint %}

{% swagger method="post" path="transparency-request" baseUrl="https://api.brickverse.co/v2/user/" summary="Information" %}
{% swagger-description %}
API request transparency records of your account data. Record data will be shipped to your email address on record. Some data will not be shown such as passwords.
{% endswagger-description %}

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
{"status": "error", "message": "reason_string"}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}

