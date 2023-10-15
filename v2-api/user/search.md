# search

{% swagger method="post" path="/search" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to search for accounts by partial strings.
{% endswagger-description %}

{% swagger-parameter in="body" name="username" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "data": [
        {
            "username": "ArkInfinity",
            "id": 2,
            "flags": {
                "admin": "Manager",
                "verified_account": true,
                "bot_account": false,
                "ugc_program": true,
                "dev_program": false
            },
            "flags_html": "<img height=\"12\" width=\"12\" alt='BrickVerse Staff' class='avimg' src='https://cdn.brickverse.co/img/brand/Admin.png'> <img height=\"12\" width=\"12\" alt='BrickVerse Verified' class='avimg' src='https://cdn.brickverse.co/img/brand/Verified.png'> ",
            "headshot": "https://cdn.brickverse.co/cache/avatars/Default_Head.png",
            "bodyshot": "https://cdn.brickverse.co/cache/avatars/Default.png"
        }
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
