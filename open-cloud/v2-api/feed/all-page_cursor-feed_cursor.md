# all/{page\_cursor/{feed\_cursor}

{% swagger method="get" path="/all/{page_cursor/{feed_cursor}" baseUrl="https://api.brickverse.gg/v2/feed" summary="Information" %}
{% swagger-description %}
API to send to your user feed.
{% endswagger-description %}

{% swagger-parameter in="path" name="page_cursor" type="Int" required="true" %}
Page Number. Utilize 0 for first page. Index key "pages" in JSON Response for the total pages.
{% endswagger-parameter %}

{% swagger-parameter in="path" name="feed_cursor" type="Int" required="true" %}
Amount of feed posts per page. Must be 0-8. Defaults to 4.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{
    "status": "ok",
    "pages": 2,
    "page_cursor": 0,
    "data": [
        {
            "post_id": 17,
            "thumbnail": "https:\/\/cdn.brickverse.gg\/cache\/avatars\/Default_Head.png",
            "message": "what&#039;s popin alex?",
            "message_raw": "what&#039;s popin alex?",
            "poster_id": 2,
            "poster_username": "ArkInfinity",
            "posted_stamp": 1706133248,
            "posted_elapsed": "1 week ago",
            "replies": []
        },
        {
            "post_id": 15,
            "thumbnail": "https:\/\/cdn.brickverse.gg\/cache\/avatars\/Default_Head.png",
            "message": "reporting to moderaiton rn.",
            "message_raw": "reporting to moderaiton rn.",
            "poster_id": 43,
            "poster_username": "Alex",
            "posted_stamp": 1705975706,
            "posted_elapsed": "1 week ago",
            "replies": []
        },
        {
            "post_id": 14,
            "thumbnail": "https:\/\/cdn.brickverse.gg\/cache\/avatars\/Default_Head.png",
            "message": "Based man in a based world",
            "message_raw": "Based man in a based world",
            "poster_id": 43,
            "poster_username": "Alex",
            "posted_stamp": 1705953858,
            "posted_elapsed": "1 week ago",
            "replies": []
        },
        {
            "post_id": 13,
            "thumbnail": "https:\/\/cdn.brickverse.gg\/cache\/avatars\/Default_Head.png",
            "message": "What&#039;s poppin",
            "message_raw": "What&#039;s poppin",
            "poster_id": 43,
            "poster_username": "Alex",
            "posted_stamp": 1705953271,
            "posted_elapsed": "1 week ago",
            "replies": []
        },
        {
            "post_id": 10,
            "thumbnail": "https:\/\/cdn.brickverse.gg\/cache\/avatars\/Default_Head.png",
            "message": "Hi mom!",
            "message_raw": "Hi mom!",
            "poster_id": 2,
            "poster_username": "ArkInfinity",
            "posted_stamp": 1705712245,
            "posted_elapsed": "2 weeks ago",
            "replies": []
        }
    ]
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
