# list

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/cloud/bricklinks/list`

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "list": [
        "id": 1,
        "expire": unix epoch timestamp,
        "redirect": "https://togosite.com",
        "token": "urlshortid",
        "owner": 1
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
