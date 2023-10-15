# v1/user/search

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/search" method="post" summary="Search Users" %}
{% swagger-description %}
This endpoint allows you to search for users in the BrickVerse Database.
{% endswagger-description %}

{% swagger-parameter in="header" name="Authentication" type="string" %}
Authentication token. For public usage use token "public"
{% endswagger-parameter %}

{% swagger-parameter in="body" name="username" type="string" %}
Part of or full username of player.
{% endswagger-parameter %}

{% swagger-response status="200" description="User Found" %}
```
{
    "status": "success",
    "data": [{
        "username": "ArkInfinity",
        "id": "4",
        "avatar_url": "https:\/\/brickverse.co\/assets\/img\/male.png"
    }]
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error", "error" => "no results"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="success" %}
Function Operational as 6/28/2021 2:44 AM PDT
{% endhint %}
