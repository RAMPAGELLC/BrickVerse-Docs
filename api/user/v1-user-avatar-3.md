# v1/user/verify-password

{% hint style="danger" %}
This API is used for challenges for users to verify password before they can do some actions such as changing password, change email, etc.
{% endhint %}

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/verify-password" method="post" summary="Verify Password" %}
{% swagger-description %}
Password challenge.
{% endswagger-description %}

{% swagger-parameter in="body" name="password" type="String" required="true" %}
Password (case sensitive)
{% endswagger-parameter %}

{% swagger-parameter in="body" name="challenge" type="String" %}
Challenge ID
{% endswagger-parameter %}

{% swagger-response status="200" description="Valid & Callback to active challenge." %}
```
{"success": true}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="Invalid challenge or password. Callback to active challenge for failure." %}
```javascript
{"success": false}
```
{% endswagger-response %}
{% endswagger %}
