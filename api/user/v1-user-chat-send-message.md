# v1/user/chat/send-message

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/chat/send-message" method="post" summary="" %}
{% swagger-description %}
his endpoint sends message.
{% endswagger-description %}

{% swagger-parameter in="body" name="content" type="string" %}
Chat Message
{% endswagger-parameter %}

{% swagger-parameter in="body" name="chatId" type="number" %}
Chat ID
{% endswagger-parameter %}

{% swagger-parameter in="body" name="token" type="string" %}
Authorization Token of user
{% endswagger-parameter %}

{% swagger-response status="200" description="Message Sent!" %}
```
{
    "status": "success"
}
```
{% endswagger-response %}

{% swagger-response status="304" description="" %}
```
{"status": "content-too-long"}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="danger" %}
Non Opertional
{% endhint %}
