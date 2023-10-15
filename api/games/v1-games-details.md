# v1/games/details

{% swagger baseUrl="https://api.brickverse.co" path="/v1/games/details" method="post" summary="Game Information" %}
{% swagger-description %}
This endpoint allows you to see game details.
{% endswagger-description %}

{% swagger-parameter in="body" name="target" type="number" %}
Game ID
{% endswagger-parameter %}

{% swagger-response status="200" description="Friends Found!" %}
```
{
    "status": "success",
    "players": 30,
    "gameid": 12345,
    "gamename": "Adopt Me!"
    "owner": 1,
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error", "error" => "no data found"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="danger" %}
Non-Operational as 6/30/2021 7:35 AM PDT. Under going changes
{% endhint %}
