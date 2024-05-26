# unread

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/notifications/unread`

API used to fetch all notifications.

#### Query Parameters

| Name       | Type    | Description                           |
| ---------- | ------- | ------------------------------------- |
| mark\_read | Boolean | Marks all notifications read if true. |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "data": [
        {
            "alert_id": 1,
            "message": "2000 have been deposited to your account, your cubes total is now 2000. Your next automatic reward will be sent in 30 days, if your plan is canceled before then you will not receive the cubes.",
            "redirect": "https:\/\/www.brickverse.co\/upgrade",
            "time": 1687911353,
            "read": true,
            "img": ""
        }
    ]
}
```
{% endtab %}

{% tab title="403: Forbidden " %}
```json
{"status": "error", "message": "No authorized BrickVerse account detected. Please login."}
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
    "message": reason
}
```
{% endtab %}
{% endtabs %}
