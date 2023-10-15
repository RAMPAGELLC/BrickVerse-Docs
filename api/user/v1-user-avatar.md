# v1/user/avatar

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/avatar" method="post" summary="Search Users" %}
{% swagger-description %}
This endpoint allows you to get avtar URL of an user, this doesn't generate a render.
{% endswagger-description %}

{% swagger-parameter in="body" name="id" type="Int" required="true" %}
Player User ID
{% endswagger-parameter %}

{% swagger-parameter in="body" name="type" type="String" %}
Render Type
{% endswagger-parameter %}

{% swagger-response status="200" description="User Found" %}
```
{
    "status": "success",
    "avatar": "https://cdn.brickverse.co/avatars/example.png"
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "error", "reason" => "no results"}
```
{% endswagger-response %}
{% endswagger %}

## Errors

|          Error         |                         Fix                         |
| :--------------------: | :-------------------------------------------------: |
| no player id specified |      Must include "id" in body of your request      |
|    invalid player id   |         We couldnt validate ID was a intval.        |
|   invalid render type  | Valid types are "player\__head" and "player\_body"_ |

Type is optional and will default to player\_head.
