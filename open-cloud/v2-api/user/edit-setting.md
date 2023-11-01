# edit-setting

{% hint style="warning" %}
Account authentication required. Read about account authentication at [https://developers.brickverse.co/v2-api/auth/bot-login](https://developers.brickverse.co/v2-api/auth/bot-login).
{% endhint %}

{% swagger method="post" path="/edit-setting" baseUrl="https://api.brickverse.co/v2/user" summary="Information" %}
{% swagger-description %}
API used to modify account settings.
{% endswagger-description %}

{% swagger-parameter in="body" name="setting_name" type="String" required="true" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="setting_value" type="Any" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "success": true}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{"status": "error", "message": "reason_string"}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="" %}
```json
{"status": "error", "message": "reason_string"}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}

## Setting Types

| Name                     | About                                                                             |
| ------------------------ | --------------------------------------------------------------------------------- |
| Blurb                    | -                                                                                 |
| Gender                   | Profile Gender. (Valid types: Male and Female)                                    |
| Social\_{SocialPlatform} | Update social username. Valid socials are: YouTube, Twitch, Twitter, and Discord. |
| Phone                    | -                                                                                 |
| Username                 | -                                                                                 |
| Email                    | -                                                                                 |
| DOB                      | -                                                                                 |
