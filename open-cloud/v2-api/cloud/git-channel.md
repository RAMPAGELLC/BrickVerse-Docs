# git/{channel}

{% swagger method="get" path="/git/{channel}" baseUrl="https://api.brickverse.co/v2/cloud" summary="Information" %}
{% swagger-description %}
Get public git activity log (recent 30 days) for a specific development channel. This is used for the public updates log on the site.
{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
No documented response.
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

## Channels

* site
* site-beta
* client
* client-beta

