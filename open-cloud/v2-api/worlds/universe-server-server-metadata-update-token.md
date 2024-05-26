# /{universe}/{server}/server/metadata/update/{token}

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/worlds/{universe_id}/{server_id}/server/metadata/update/{host_token}`

Update server metadata such as Ping & In-game players. This API is used internally only. Falsified data breaches the BrickVerse ToS.

#### Request Body

| Name                                      | Type           | Description |
| ----------------------------------------- | -------------- | ----------- |
| players<mark style="color:red;">\*</mark> | Array          |             |
| ping<mark style="color:red;">\*</mark>    | Float\|Integer |             |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true, "connection": "49152.group.vanex.brickverse.co", "port": 3000}
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
{"status": "error", "message": "reason_string"}
```
{% endtab %}
{% endtabs %}
