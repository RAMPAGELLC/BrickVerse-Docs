# v1/user/chat/chat-summary

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/chat/chat-summary" method="post" summary="" %}
{% swagger-description %}
This endpoint returns a table of the chat summary
{% endswagger-description %}

{% swagger-parameter in="query" name="chatId" type="number" %}
ID Of Chat
{% endswagger-parameter %}

{% swagger-parameter in="body" name="token" type="string" %}
Authorization Token of user
{% endswagger-parameter %}

{% swagger-response status="200" description="Summary Found" %}
```
{
    "status": "success",
    "data": [{
        members: [{
         "username": "nate",
         "id": "6",
         "avatar_url": "https:\/\/brickverse.co\/assets\/img\/male.png",
        }],
        "chat_id": "1",
        "member_count": "1",
        "chat_name": "epic friends chat!"
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
