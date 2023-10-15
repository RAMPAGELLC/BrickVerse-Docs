# v1/wear

{% hint style="warning" %}
This endpoint requires a Brick Session.
{% endhint %}

{% swagger method="get" path="/wear" baseUrl="https://api.brickverse.co/v1/character" summary="" %}
{% swagger-description %}
This endpoint allows you to put an asset on your character.
{% endswagger-description %}

{% swagger-parameter in="query" type="Int" required="true" name="id" %}
Item ID
{% endswagger-parameter %}

{% swagger-parameter in="query" name="type" type="String" required="true" %}
Item Type (Hat, Shirt, etc)
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response is OK if successful" %}
```javascript
Response of RES-Avatar Render URL then OK.
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="Unsuccessful body responses" %}
```javascript
ERR-Invalid item type // Invalid item type.
ERR:notloggedin // No BRICK SESSION
```
{% endswagger-response %}
{% endswagger %}

## Valid Types

* shirt
* hat
* pants
* tool
* face
* hat

API will refuse to wear:

* texture
* sound

tool section of brickverse is NOT completed.
