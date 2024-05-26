# edit-setting

{% hint style="warning" %}
Account authentication required. Read about account authentication at [https://developers.brickverse.co/v2-api/auth/bot-login](https://developers.brickverse.co/v2-api/auth/bot-login).
{% endhint %}

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/user/edit-setting`

API used to modify account settings.

#### Request Body

| Name                                             | Type   | Description |
| ------------------------------------------------ | ------ | ----------- |
| setting\_name<mark style="color:red;">\*</mark>  | String |             |
| setting\_value<mark style="color:red;">\*</mark> | Any    |             |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true}
```
{% endtab %}

{% tab title="403: Forbidden " %}
```json
{"status": "error", "message": "reason_string"}
```
{% endtab %}

{% tab title="429: Too Many Requests " %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endtab %}

{% tab title="400: Bad Request " %}
```json
{"status": "error", "message": "reason_string"}
```
{% endtab %}
{% endtabs %}

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
