# v1/user/get-messages

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/chat/get-messages" method="post" summary="" %}
{% swagger-description %}
This endpoint returns a table of the current messages
{% endswagger-description %}

{% swagger-parameter in="query" name="page" type="string" %}
page id
{% endswagger-parameter %}

{% swagger-parameter in="query" name="startId" type="string" %}
start id
{% endswagger-parameter %}

{% swagger-parameter in="query" name="chatId" type="number" %}
ID Of Chat
{% endswagger-parameter %}

{% swagger-parameter in="body" name="token" type="string" %}
Authorization Token of user
{% endswagger-parameter %}

{% swagger-response status="200" description="Summary Found" %}
```
{}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="danger" %}
Non Opertional, we're still drafting this backend up.
{% endhint %}

