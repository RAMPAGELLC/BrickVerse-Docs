# register

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/user/register`

API used to register accounts.

#### Request Body

| Name                                             | Type   | Description                         |
| ------------------------------------------------ | ------ | ----------------------------------- |
| username<mark style="color:red;">\*</mark>       | String |                                     |
| password<mark style="color:red;">\*</mark>       | String |                                     |
| email<mark style="color:red;">\*</mark>          | String |                                     |
| gender<mark style="color:red;">\*</mark>         | String |                                     |
| tos\_agree<mark style="color:red;">\*</mark>     | Bool   |                                     |
| child\_account<mark style="color:red;">\*</mark> | Bool   | If registered as a minor account.   |
| parent\_email                                    | String | Required if child\_account is true. |
| captcha<mark style="color:red;">\*</mark>        | String |                                     |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true}
```
{% endtab %}

{% tab title="403: Forbidden " %}
```json
{"status": "error", "message": 403}
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
