# version

{% swagger method="get" path="/version" baseUrl="https://api.brickverse.co/v2/cloud" summary="Information" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "message": "OpenCloud API v2 Version information located.",
    "version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-vq9oisbetterdev",
    "log": {
        "version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-vq9oisbetterdev",
        "title": "What's new",
        "art": "https:\/\/cdn.brickverse.gg\/img\/art\/intro.png",
        "published": "Published on November 28, 2023",
        "body": "Make sure to join our community discord, we are still working daily on new features.",
        "headlines": [
            {
                "headline": "SITE",
                "changes": [
                    "Speed improvements.",
                    "New payment proccesser completed.",
                    "Currency purchase amount has been lowered, they still maintain the same valuation",
                    "Other misc fixes."
                ]
            },
            {
                "headline": "ENGINE",
                "changes": [
                    "BrickLua API.",
                    "Backend Draft."
                ]
            }
        ],
        "previous_version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-franyisgooddev69",
        "previous": {
            "version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-franyisgooddev69",
            "title": "What's new",
            "art": "https:\/\/cdn.brickverse.gg\/img\/art\/intro.png",
            "published": "Published on November 26, 2023",
            "body": "Make sure to join our community discord.",
            "headlines": [
                {
                    "headline": "SITE",
                    "changes": [
                        "New changes modal",
                        "Site security improvements",
                        "Speed improvements"
                    ]
                },
                {
                    "headline": "ENGINE",
                    "changes": [
                        "BrickLua API",
                        "Backend Draft"
                    ]
                }
            ]
        }
    }
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
