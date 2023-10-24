# get-active-sessions

{% swagger method="get" path="/get-active-sessions" baseUrl="https://api.brickverse.co/v2/auth" summary="Information" expanded="false" %}
{% swagger-description %}
Get current active sessions.

Token field is always false and used internally.
{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "success": true,
    "sessions": [
        {
            "session_id": 1,
            "device": "Windows",
            "browser": "Google Chrome",
            "created": "2023-10-21 17:21:43",
            "location": {
                "ip": "IPv4",
                "type": "local",
                "city": "CITY",
                "region_name": "REGION",
                "region_code": "RG",
                "zip": "97301",
                "country_name": "COUNTRY",
                "country_code": "CC",
                "continent_code": "CC",
                "continent_name": "CONTINET",
                "latitude": 1,
                "longitude": 1
            },
            "is_staff": true,
            "same_device": true,
            "token": false
        }
    ]
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{"status": "error", "message": "reason_string"}
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
