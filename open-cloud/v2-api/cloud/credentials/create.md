# create

{% swagger method="post" path="/create" baseUrl="https://api.brickverse.co/v2/cloud/credentials" summary="Information" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="body" name="ownerId" type="Int" required="true" %}
0 for authenticated user, anything above 0 will be taken as a Guild.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "apiKey": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "apiSecret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "apiId": 99999999999
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
