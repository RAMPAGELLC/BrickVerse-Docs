# register

{% swagger method="post" path="/register" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to register accounts.
{% endswagger-description %}

{% swagger-parameter in="body" name="username" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="String" required="true" name="password" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="captcha" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="String" required="true" name="email" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="String" required="true" name="gender" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="Bool" required="true" name="tos_agree" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="child_account" type="Bool" required="true" %}
If registered as a minor account.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="parent_email" type="String" %}
Required if child\_account is true.
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
