# /{universe}/{server}/server/metadata/update/{token}

{% swagger method="post" path="/{server_id}/server/metadata/update/{host_token}" baseUrl="https://api.brickverse.co/v2/worlds/{universe_id}" summary="Information" expanded="false" %}
{% swagger-description %}
Update server metadata such as Ping & In-game players. This API is used internally only. Falsified data breaches the BrickVerse ToS.
{% endswagger-description %}

{% swagger-parameter in="body" name="players" required="true" type="Array" %}

{% endswagger-parameter %}

{% swagger-parameter in="body" name="ping" type="Float|Integer" required="true" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "success": true, "connection": "49152.group.vanex.brickverse.co", "port": 3000}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="" %}
```json
{"status": "error", "message": "reason_string"}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="" %}
```json
{"status": "error", "message": 403}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}
