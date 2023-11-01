# vanex-details

{% swagger method="get" path="/vanex-details/{world_id}/{host_token}" baseUrl="https://api.brickverse.co/v2/worlds/{universe_id}" summary="Information" expanded="false" %}
{% swagger-description %}
Fetch server details such as Connection A Record, Port, etc.
{% endswagger-description %}

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
