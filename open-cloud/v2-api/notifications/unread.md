# unread

{% swagger method="get" path="/unread" baseUrl="https://api.brickverse.co/v2/notifications" summary="Information" %}
{% swagger-description %}
API used to fetch all notifications.
{% endswagger-description %}

{% swagger-parameter in="query" name="mark_read" type="Boolean" %}
Marks all notifications read if true.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "data": [
        {
            "alert_id": 1,
            "message": "2000 have been deposited to your account, your cubes total is now 2000. Your next automatic reward will be sent in 30 days, if your plan is canceled before then you will not receive the cubes.",
            "redirect": "https:\/\/www.brickverse.co\/upgrade",
            "time": 1687911353,
            "read": true,
            "img": ""
        }
    ]
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{
    "status": "error",
    "message": reason
}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="" %}
```json
{"status": "error", "message": "No authorized BrickVerse account detected. Please login."}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}
