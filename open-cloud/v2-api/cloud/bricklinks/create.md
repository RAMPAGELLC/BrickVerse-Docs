# create

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/cloud/bricklinks/create`

#### Request Body

| Name                                     | Type   | Description                                       |
| ---------------------------------------- | ------ | ------------------------------------------------- |
| url<mark style="color:red;">\*</mark>    | String | Valid URL                                         |
| expire<mark style="color:red;">\*</mark> | Int    | UNIX Timestamp expiration. Enter 0 for no expiry. |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "message" => "Brickl.ink URL created!",
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
