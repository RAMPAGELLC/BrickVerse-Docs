# create

{% swagger method="post" path="/create" baseUrl="https://api.brickverse.co/v2/cloud/bricklinks" summary="Information" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="body" name="url" type="String" required="true" %}
Valid URL
{% endswagger-parameter %}

{% swagger-parameter in="body" type="Int" name="expire" required="true" %}
UNIX Timestamp expiration. Enter 0 for no expiry.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "message" => "Brickl.ink URL created!",
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{
    "status": "error",
    "message": "Invalid request, missing some post fields.",
    "got": null
}
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
