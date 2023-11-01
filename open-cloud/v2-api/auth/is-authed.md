# is-authed

{% swagger method="get" path="/is-authed" baseUrl="https://api.brickverse.co/v2/auth" summary="Information" expanded="false" %}
{% swagger-description %}
Check if a user is currently authenticated.
{% endswagger-description %}

{% swagger-response status="200: OK" description="User is logged in." %}

{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="User is not logged in." %}

{% endswagger-response %}
{% endswagger %}
