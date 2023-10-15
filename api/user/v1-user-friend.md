# v1/user/friend

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/friend" method="post" summary="Add Friend" %}
{% swagger-description %}
This endpoint allows you to create friend requests.
{% endswagger-description %}

{% swagger-parameter in="body" name="token" type="string" required="true" %}
Account Token of Sender
{% endswagger-parameter %}

{% swagger-parameter in="body" name="target" type="number" required="true" %}
UserId of target to add
{% endswagger-parameter %}

{% swagger-response status="200" description="Request Created" %}
```
{
    "status": "success",
    "message": "sent"
}
```
{% endswagger-response %}

{% swagger-response status="302" description="Already Friends" %}
```
{
    "status": "success",
    "message": "active friends"
}
```
{% endswagger-response %}

{% swagger-response status="304" description="Active Request" %}
```
{
    "status": "success",
    "message": "active request"
}
```
{% endswagger-response %}

{% swagger-response status="400" description="Invalid Token" %}
```
{"status": "error", "error" => "bad token"}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error", "error" => "no results"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="success" %}
Function Operational as 7/31/2021 8:30 PM PDT
{% endhint %}

{% hint style="info" %}
Function Updated @ 8/1/2021 9:08 PM PDT
{% endhint %}

