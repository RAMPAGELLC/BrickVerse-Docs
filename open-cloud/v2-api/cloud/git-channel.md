# git/{channel}

## Information

<mark style="color:blue;">`GET`</mark> `https://api.brickverse.co/v2/cloud/git/{channel}`

Get public git activity log (recent 30 days) for a specific development channel. This is used for the public updates log on the site.

{% tabs %}
{% tab title="200: OK Response" %}
```json
No documented response.
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

## Channels

* site
* site-beta
* client
* client-beta

