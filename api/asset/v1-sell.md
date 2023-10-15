# v1/sell

{% hint style="danger" %}
This endpoint is dedicated to production usage of BrickVerse & not recommended for 3rd Party applications due to cookie requirement & way we handle data on this endpoint.
{% endhint %}

{% swagger method="get" path="/sell" baseUrl="https://api.brickverse.co/v1/asset" summary="" %}
{% swagger-description %}
This endpoint allows you to sell your limited.
{% endswagger-description %}

{% swagger-parameter in="query" name="itemid" type="Int" required="true" %}
Asset ID
{% endswagger-parameter %}

{% swagger-parameter in="query" name="serial" type="Int" required="true" %}
Serial ID
{% endswagger-parameter %}

{% swagger-parameter in="query" name="price" type="Int" required="true" %}
Resell Amount
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Basic Response" %}
```javascript
Redirection to catalog view page of item. Hence API usage should NOT be used for v1/asset
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="Errors for invalid data." %}
```javascript
ERR:inv // You do not own that serial
ERR:osa // Item already on sale
err:nl // Item is not a limited
```
{% endswagger-response %}
{% endswagger %}

{% hint style="info" %}
Due to this endpoint not returning JSON, you can parse the body with Javascript. Heres a example.
{% endhint %}

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', "/api/v1/asset/purchase?id=1", true);

xhr.onload = function() {
    var data = xhr.response;
    
    if (data.startsWith("success")) {
        console.log("Purchase successful!");
    } else {
        var reason = data.split(":")[1];
        console.log("Purchase failed for " + reason);
    }
};

xhr.send();
```

This endpoint is used for selling limited items.
