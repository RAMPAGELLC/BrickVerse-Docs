# get-token

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/auth/get-token`

Fetch active session's BrickVerse Security token.

Sharing this token allows anyone to login as you.

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true, "token": "token"}
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
