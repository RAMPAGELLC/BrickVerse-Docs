# v1/join

{% swagger method="get" path="/join" baseUrl="https://api.brickverse.co/v1/guild" summary="" %}
{% swagger-description %}
Join guild.
{% endswagger-description %}

{% swagger-parameter in="query" name="id" type="Int" required="true" %}
Guild ID
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Success" %}
```javascript
Redirected to guild once joined.
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="Error" %}
```javascript
Body will be full error, example: Pending Join Request!
```
{% endswagger-response %}
{% endswagger %}
