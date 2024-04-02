# create

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/cloud/oauth/create`

#### Request Body

EMPTY

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "appId": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "apiSecret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
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

Create a new OAuth Application.
