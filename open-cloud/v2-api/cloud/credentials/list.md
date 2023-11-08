# list

{% swagger method="get" path="/list/{list-type}..." baseUrl="https://api.brickverse.co/v2/cloud/credentials" summary="Information" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="path" name="guild/{guild-id}" required="true" %}
List all current API keys for the guild.
{% endswagger-parameter %}

{% swagger-parameter in="path" name="user" required="true" %}
List all current API keys for the authenticated account.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "list": [
        "apiKey": "XXXXXXXXXXXXXXXXXXXX",
        "created": unix epoch timestamp,
        "apiId": 222222222222,
        "ownerId": 1,
        "ownerType": "USER"
    ]
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
