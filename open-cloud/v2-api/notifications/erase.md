# erase

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/notifications/erase`

API used to erase all notifications.

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "success": true
}
```
{% endtab %}

{% tab title="403: Forbidden " %}
```json
{"status": "error", "message": "No authorized BrickVerse account detected. Please login."}
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
    "message": reason
}
```
{% endtab %}
{% endtabs %}
