# send-beta-key

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/auth/send-beta-key/{email}`

Forward your beta key to your e-mail address.

Account registered with the e-mail is required.

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "success": true,
    "message": ...
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
{"status": "error", "message": ...}
```
{% endtab %}
{% endtabs %}
