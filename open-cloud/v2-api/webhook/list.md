# list

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/webhook/list`

API used to list webhooks you have created.

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "list": [
        {
            "id": 1,
            "ownerid": 1,
            "url": "https://127.0.0.1",
            "created": 000000000
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
{
    "status": "error",
    "message": "Invalid request, missing some post fields.",
    "got": null
}
```
{% endtab %}
{% endtabs %}
