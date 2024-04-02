# list

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/cloud/credentials/list/{list-type}...`

#### Path Parameters

| Name                                               | Type   | Description                                              |
| -------------------------------------------------- | ------ | -------------------------------------------------------- |
| user<mark style="color:red;">\*</mark>             | String | List all current API keys for the authenticated account. |
| guild/{guild-id}<mark style="color:red;">\*</mark> | String | List all current API keys for the guild.                 |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "list": [
        "apiKey": "XXXXXXXXXXXXXXXXXXXX",
        "created": unix epoch timestamp,
        "apiId": 222222222222,
        "ownerId": 1,
        "ownerType": "USER"
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
