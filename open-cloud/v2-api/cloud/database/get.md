# get

{% hint style="danger" %}
**Requires OpenCloud Authentication**
{% endhint %}

{% swagger method="get" path="/get" baseUrl="https://api.brickverse.co/v2/cloud/database" summary="Information" %}
{% swagger-description %}
API used to delete a specific webhook
{% endswagger-description %}

{% swagger-parameter in="body" name="worldId" type="Int" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="dataKey" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "data": [
        "UID": 000,
        "WorldId": 001,
        "StoreKey": "CoolKey",
        "StoreValue": [
            "JSONRocks": true
        ],
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
