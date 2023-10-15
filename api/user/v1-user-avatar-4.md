# v1/user/login

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/get-token" method="post" summary="Login" %}
{% swagger-description %}
This endpoints logs you in with brick session.
{% endswagger-description %}

{% swagger-parameter in="query" name="token" required="true" type="String" %}
Brick Session ID
{% endswagger-parameter %}

{% swagger-response status="200" description="User Found" %}
```
Redirected to dashboard.
```
{% endswagger-response %}
{% endswagger %}
