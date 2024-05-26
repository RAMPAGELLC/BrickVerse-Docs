# create

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/webhook/create`

API used to create webhooks.

#### Request Body

| Name                                  | Type   | Description                                                                      |
| ------------------------------------- | ------ | -------------------------------------------------------------------------------- |
| URL<mark style="color:red;">\*</mark> | String | Ensure you have a Port defined for IPv4's if required. (Example: 127.0.0.1:3000) |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
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
