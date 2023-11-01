# join-game

{% hint style="danger" %}
**DANGEROUS ENDPOINT!** SHARING YOUR **JOIN KEY** WILL ALLOW ANYONE WHO HAS IT TO ACCESS YOUR **BRICKVERSE.CO ACCOUNT**!
{% endhint %}

{% swagger method="get" path="/join-game/{join_key}" baseUrl="https://api.brickverse.co/v2/auth" summary="Information" expanded="false" %}
{% swagger-description %}
Data for internal engine to login as you for internal services within the client. This will NOT launch a connection to a game. To connect to a game use URL Protocol brickverse://join@{join\_key}
{% endswagger-description %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "success": true,
    "user_data": {
        "status": "ok",
        "found": true,
        "avatar_data": {
            "Data": {
                "Face": 0,
                "Hats": [],
                "Tool": 0,
                "Pants": 0,
                "Shirt": 0,
                "TShirt": 0,
                "Max_Hats": 3
            },
            "Color": {
                "Head": "#e2e2e2",
                "Torso": "#949191",
                "LeftArm": "#e2e2e2",
                "LeftLeg": "#e2e2e2",
                "RightArm": "#e2e2e2",
                "RightLeg": "#e2e2e2"
            }
        },
        "user_data": {
            "headshot": "https:\/\/cdn.brickverse.co\/cache\/avatars\/Default_Head.png",
            "bodyshot": "https:\/\/cdn.brickverse.co\/cache\/avatars\/Default.png",
            "original_username": "System",
            "username": "System",
            "username_history": [
                "System"
            ],
            "suspended": false,
            "rank": "Member",
            "membership": "NONE",
            "gender": "Male",
            "asset_storage_limit": 300,
            "game_info": {
                "GameId": 0,
                "InGame": false,
                "ServerId": 0
            },
            "flags": {
                "rank": "Member",
                "admin": false,
                "verified_account": true,
                "verified_id": false,
                "gov_official": false,
                "bot_account": true,
                "ugc_program": false,
                "dev_program": false
            },
            "flags_html": "  <img height=\"25\" width=\"25\" alt='BrickVerse Verified' class='avimg' src='https:\/\/cdn.brickverse.co\/img\/brand\/Verified.png'>  <img height=\"25\" width=\"25\" alt='Bot Account' class='avimg' src='https:\/\/cdn.brickverse.co\/img\/brand\/Bot.png'>",
            "last": {
                "online": 1695260907,
                "play": 1690305296
            }
        }
    },
    "server_data": {
        "ip": "127.0.0.1",
        "port": 49152,
        "join_key": "KEY_SCRUBBED",
        "join_key_expired": true
    }
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{"status": "error", "message": "reason_string"}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="" %}
```json
{"status": "error", "message": 403}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}
