# login

{% swagger method="post" path="/login" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to log into accounts.
{% endswagger-description %}

{% swagger-parameter in="body" name="username" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="String" required="true" name="password" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="captcha" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="login_method" type="String" required="true" %}
Default: **Password**. Options: **SMS, Password, Email**
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
<pre class="language-json"><code class="lang-json"><strong>{"status": "error", "message": 403}
</strong>
// You will recieve a 403 response if a user requires two-step authentication.
{"status": "error", "message": "Two Step verification required", "vsid": "{vsid}"}
</code></pre>
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}
