# create

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/cloud/credentials/create`

#### Request Body

<table><thead><tr><th width="193">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td>ownerId<mark style="color:red;">*</mark></td><td>Int</td><td>0 for authenticated user, anything above 0 will be taken as a Guild.</td></tr><tr><td>expire<mark style="color:red;">*</mark></td><td>Int</td><td>UNIX Timestamp expiration. Enter 0 for no expiry.</td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Response" %}
```json
{
    "status": "ok",
    "apiKey": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "apiSecret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "apiId": 99999999999
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
