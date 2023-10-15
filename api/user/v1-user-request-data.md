# v1/user/request-data

{% swagger method="post" path="/request-data" baseUrl="https://api.brickverse.co/v1/user" summary="Request Data" %}
{% swagger-description %}
Request account data we have on your account. We will NOT add an endpoint to delete your account due to the fact we don't want users being malicious links have you delete your account.\
\
This endpoint does NOT share your data, it will only send an email to logged in account. this endpoint is for transparency and is used for the "Request Data" action in settings.
{% endswagger-description %}

{% swagger-response status="200: OK" description="Email sent" %}
```javascript
{"success": true}
```
{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="Not logged in or a error occured" %}
```javascript
{"success": false}
```
{% endswagger-response %}
{% endswagger %}
