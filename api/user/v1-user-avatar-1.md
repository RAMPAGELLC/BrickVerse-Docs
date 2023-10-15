# v1/user/get-by-username

{% swagger baseUrl="https://api.brickverse.co" path="/v1/user/get-by-username" method="post" summary="Search Users" %}
{% swagger-description %}
Get a user by username.
{% endswagger-description %}

{% swagger-parameter in="query" name="username" required="true" type="String" %}
Player Username
{% endswagger-parameter %}

{% swagger-response status="200" description="User Found" %}
```
{
    "status": "success",
    "username": "ArkInfinity",
    "id": 3,
    "cubes": 500,
    "plan": "LEVEL_3",
    "rank": "Manager",
    "avatar_body": "generatedurl.png",
    "avatar_head": "generatedurl.png"
}
```
{% endswagger-response %}

{% swagger-response status="404" description="No results found in the database." %}
```
{"status": "failed", "reason" => "no results"}
```
{% endswagger-response %}
{% endswagger %}

## Errors

|           Error          |            Fix           |
| :----------------------: | :----------------------: |
| Username wasn't found. 1 | No username found in GET |
| Username wasn't found. 2 |    No database results   |

## Data Explained

LEVEL_3 = Gold Plan._\
_LEVEL_2 = Silver Plan\
LEVEL\_1  = Bronze Plan\
Member = Non-Plan.

Manager = Highest Staff Rank\
Administrator = Highly trusted staff.\
Moderator = Staff\
Member = Player
