# v1/user/friends

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/friends" method="post" summary="View Friends" %}
{% swagger-description %}
This endpoint allows you to see active-friends.
{% endswagger-description %}

{% swagger-parameter in="body" name="target" type="number" %}
UserId of the user
{% endswagger-parameter %}

{% swagger-response status="200" description="Friends Found!" %}
```
{
    "status": "success",
    "data": [{
        "username": "nate",
        "id": "6",
        "avatar_url": "https:\/\/brickverse.co\/assets\/img\/male.png"
    }]
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error", "error" => "User has no friends"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="success" %}
Operational as 6/28/2021 2:44 AM PDT.
{% endhint %}
