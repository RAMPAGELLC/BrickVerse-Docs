# v1/take-offsale

{% hint style="danger" %}
This endpoint is dedicated to production usage of BrickVerse & not recommended for 3rd Party applications due to cookie requirement & way we handle data on this endpoint.
{% endhint %}

{% swagger method="get" path="/take-offsale" baseUrl="https://api.brickverse.co/v1/asset" summary="" %}
{% swagger-description %}
This endpoint allows you to take your resold limited offsale.
{% endswagger-description %}

{% swagger-parameter in="query" name="id" type="Int" required="true" %}
Asset ID
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Basic Response" %}
```javascript
Redirection to catalog view page of item. Hence API usage should NOT be used for v1/asset
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="Errors for invalid data." %}
```javascript
ERR:loggedout // Logged out.
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

This endpoint is used for taking your reselled limiteds offsale.
