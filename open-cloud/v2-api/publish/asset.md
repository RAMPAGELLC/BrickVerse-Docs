# Asset

{% swagger method="post" path="/publish/asset" baseUrl="https://publish.brickverse.gg" summary="Information" expanded="false" %}
{% swagger-description %}
Publish a new asset, or o new version of a existing asset.
{% endswagger-description %}

{% swagger-parameter in="query" name="assetId" required="false" type="BigInt" %}
Require to publish a new version of an existing asset.
{% endswagger-parameter %}

{% swagger-parameter in="query" name="assetType" required="true" type="String" %}
Asset Type
{% endswagger-parameter %}

{% swagger-parameter in="query" name="assetName" type="String (1-32)" %}
Asset Name. Default to: Asset {uuid}
{% endswagger-parameter %}

{% swagger-parameter in="query" name="assetDescription" type="String (1-500)" %}
Asset Description. Defaults to: No asset description.
{% endswagger-parameter %}

{% swagger-parameter in="query" type="BigInt" required="true" name="assetOwner" %}
Asset Owner ID
{% endswagger-parameter %}

{% swagger-parameter in="query" type="String" name="assetOwnerType" required="true" %}
USER or GUILD
{% endswagger-parameter %}

{% swagger-parameter in="query" name="textureId" type="BigInt" %}
Required for 3D Assets & Clothing.   This reduces repetitive assets on the CDN.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="files" type="Array" required="true" %}
File
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response" %}
```json
{"status": "ok", "success": true, "assetid": x}
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

## Asset Types

{% content-ref url="../../asset-types.md" %}
[asset-types.md](../../asset-types.md)
{% endcontent-ref %}

{% hint style="danger" %}
Files undergo automatic moderation by Artificial Intelligence. Based on the AI's analysis, files are either automatically approved or denied. Once a file is denied, it cannot be restored due to privacy and legal considerations, and it is automatically deleted. However, you can reach out to support for assistance.



Support Staff can manually upload the file for human moderation upon request, or you can include the query string "HUMAN\_MODERATE" in your API request on publish.brickverse.gg to trigger human moderation. Human Moderation can take up to 78 hours, or more depending on load of the moderation queue.
{% endhint %}

{% hint style="warning" %}
UGC Permissions Role is required to upload asset types:

* ACCESSORY
* FACE
* TOOL.
{% endhint %}
