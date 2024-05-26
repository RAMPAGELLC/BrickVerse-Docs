# terminate-session

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/auth/terminate-session/{session-id}`

Terminate a session by Session ID. You cannot terminate another user's session id as its tied to user-id requirement.

\
Upon termination of the session they will be logged out.

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
