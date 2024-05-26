# /{universe}/shutdown/all/{token}

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/worlds/{universe_id}/shutdown/all/{host_token}`

Closes all servers (including worlds under the experience, not just the root world.)

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true}
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
