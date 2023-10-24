# terminate-session

{% swagger method="post" path="/terminate-session/{session-id}" baseUrl="https://api.brickverse.co/v2/auth" summary="Information" expanded="false" %}
{% swagger-description %}
Terminate a session by Session ID. You cannot terminate another user's session id as its tied to user-id requirement.

\
Upon termination of the session they will be logged out.
{% endswagger-description %}

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
{"status": "error", "message": 403}
```
{% endswagger-response %}

{% swagger-response status="429: Too Many Requests" description="" %}
```json
{"status": "error", "message": "Rate limited", "ratelimited": true, "time": "seconds_string"}
```
{% endswagger-response %}
{% endswagger %}
