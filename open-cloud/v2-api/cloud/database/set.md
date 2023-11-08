# set

{% hint style="danger" %}
**Requires OpenCloud Authentication**
{% endhint %}

{% swagger method="post" path="/set" baseUrl="https://api.brickverse.co/v2/cloud/database" summary="Information" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="body" required="true" name="worldId" type="Int" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="String" name="dataKey" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" type="Array" name="dataValue" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok"
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
