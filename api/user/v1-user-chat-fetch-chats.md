# v1/user/chat/chats

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/chat/chats" method="post" summary="" %}
{% swagger-description %}
This endpoint returns a table of past user has been chatting with for the Chat Widget.
{% endswagger-description %}

{% swagger-parameter in="body" name="token" type="string" %}
Authorization Token of user
{% endswagger-parameter %}

{% swagger-response status="200" description="Chat Found" %}
```
{
    "status": "success",
    "data": [{
        "username": "nate",
        "id": "6",
        "avatar_url": "https:\/\/brickverse.co\/assets\/img\/male.png",
        "last_message": "hello world",
        "chat_id": "1",
        "chat_name": "BrickVerse Club"
    }]
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="danger" %}
Non Opertional
{% endhint %}
