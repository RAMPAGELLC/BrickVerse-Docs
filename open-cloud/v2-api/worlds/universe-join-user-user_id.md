# /{universe}/join/user/{user\_id}

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/worlds/{universe_id}/join/user/user_id`

User must have Public Joins enabled or must be friends.

#### Query Parameters

| Name           | Type   | Description                                                                         |
| -------------- | ------ | ----------------------------------------------------------------------------------- |
| launch\_client | Bool   | Launch brickverse client or not.                                                    |
| return\_url    | String | Redirect a user after launching the client. launch\_client query param is required. |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true, "client_join_token": "XXXXXXXXXXXXXXX"}
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
