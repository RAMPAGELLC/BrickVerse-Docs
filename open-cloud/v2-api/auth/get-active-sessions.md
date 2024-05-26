# get-active-sessions

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/auth/get-active-sessions`

Get current active sessions.

Token field is always false and used internally.

{% tabs %}
{% tab title="200: OK Response" %}
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
{% endtab %}

{% tab title="403: Forbidden " %}
```json
{"status": "error", "message": 403}
```
{% endtab %}

{% tab title="429: Too Many Requests " %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endtab %}

{% tab title="400: Bad Request " %}
```json
{"status": "error", "message": "reason_string"}
```
{% endtab %}
{% endtabs %}
