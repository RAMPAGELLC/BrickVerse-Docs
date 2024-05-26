# set

{% hint style="danger" %}
**Requires OpenCloud Authentication**
{% endhint %}

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/cloud/database/set`

#### Request Body

| Name                                        | Type   | Description |
| ------------------------------------------- | ------ | ----------- |
| worldId<mark style="color:red;">\*</mark>   | Int    |             |
| dataKey<mark style="color:red;">\*</mark>   | String |             |
| dataValue<mark style="color:red;">\*</mark> | Array  |             |

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
