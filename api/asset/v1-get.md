# v1/get

{% swagger baseUrl="https://api.brickverse.co" path="/v1/asset/get" method="get" summary="" %}
{% swagger-description %}
This endpoint allows you to get asset information
{% endswagger-description %}

{% swagger-parameter in="body" name="assetid" type="number" %}
AssetID
{% endswagger-parameter %}

{% swagger-response status="200" description="Friends Found!" %}
```
{
    "status": "success",
    "data": [{
        "id": "1",
        "name": "Baseplate",
        "type": "Universe",
        "creator": "1",
    }]
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error", "error" => "No asset could be found with that ID"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="danger" %}
Endpoint inactive. under going revamp.
{% endhint %}
