# delete

## Information

<mark style="color:red;">`DELETE`</mark> `https://api.brickverse.co/v2/cloud/bricklinks/delete/{id}`

API used to delete a specific brick link.

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok"
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
