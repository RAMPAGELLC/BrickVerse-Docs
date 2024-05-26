# login

## Information

<mark style="color:green;">`POST`</mark> `https://api.brickverse.co/v2/user/login`

API used to log into accounts.

#### Request Body

| Name                                            | Type   | Description                                              |
| ----------------------------------------------- | ------ | -------------------------------------------------------- |
| username<mark style="color:red;">\*</mark>      | String |                                                          |
| password<mark style="color:red;">\*</mark>      | String |                                                          |
| login\_method<mark style="color:red;">\*</mark> | String | Default: **Password**. Options: **SMS, Password, Email** |
| captcha<mark style="color:red;">\*</mark>       | String |                                                          |

{% tabs %}
{% tab title="200: OK Response" %}
```json
{"status": "ok", "success": true}
```
{% endtab %}

{% tab title="403: Forbidden " %}
<pre class="language-json"><code class="lang-json"><strong>{"status": "error", "message": 403}
</strong>
// You will recieve a 403 response if a user requires two-step authentication.
{"status": "error", "message": "Two Step verification required", "vsid": "{vsid}"}
</code></pre>
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
