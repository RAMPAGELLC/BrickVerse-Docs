# search

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/user/search`

API used to search for accounts by partial strings.

#### Request Body

| Name                                       | Type   | Description |
| ------------------------------------------ | ------ | ----------- |
| username<mark style="color:red;">\*</mark> | String |             |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "data": [
        {
            "username": "ArkInfinity",
            "id": 2,
            "flags": {
                "admin": "Manager",
                "verified_account": true,
                "bot_account": false,
                "ugc_program": true,
                "dev_program": false
            },
            "flags_html": "<img height=\"12\" width=\"12\" alt='BrickVerse Staff' class='avimg' src='https://cdn.brickverse.co/img/brand/Admin.png'> <img height=\"12\" width=\"12\" alt='BrickVerse Verified' class='avimg' src='https://cdn.brickverse.co/img/brand/Verified.png'> ",
            "headshot": "https://cdn.brickverse.co/cache/avatars/Default_Head.png",
            "bodyshot": "https://cdn.brickverse.co/cache/avatars/Default.png"
        }
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
