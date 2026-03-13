# Setting Up Developer Webhooks

BrickVerse Developer Webhooks allow your services to receive important platform events in real time so you can automate account handling, moderation syncing, and compliance-related workflows.

This guide explains how Developer Webhooks work, what events are currently available, and how your endpoint must respond to avoid failed deliveries.

### What Are Developer Webhooks?

A Developer Webhook is an HTTP endpoint on your server that BrickVerse can send event notifications to when certain actions occur involving users and universes you own.

When an event happens, BrickVerse sends an HTTP request to your configured webhook URL containing the event payload. Your system should process the event and immediately acknowledge receipt.

### Currently Supported Events

BrickVerse currently supports the following webhook events:

* `user.deleted`\
  Sent when a user deletes their account under GDPR right-to-forget protections and has played a universe owned by the developer.
* `user.moderated`\
  Sent when a user is banned or unbanned through developer moderation tools within a universe owned by the developer.

### Delivery Requirements

Your webhook endpoint **must** respond with:

* HTTP status code: `200`
* Response body: `OK`

This is required to successfully acknowledge the event.

{% hint style="danger" %}
If your endpoint does not return both a `200` status code and the exact body `OK`, BrickVerse will treat the delivery as failed and retry it later.
{% endhint %}

### Retry Behavior

If delivery fails, BrickVerse will continue attempting to resend the event.

Delivery retry behavior:

* BrickVerse retries approximately every **10 minutes**
* Actual retry timing may be later depending on system queue load
* After **20 failed delivery attempts**, the webhook and event will be automatically removed from the system

Because of this, your webhook endpoint should always return a valid acknowledgment as quickly as possible.

### Best Practices

To keep your webhook integration reliable:

* Return `200 OK` as soon as the event is received
* Process webhook events quickly and safely
* Make your event handling idempotent so duplicate deliveries do not cause issues
* Log failed or malformed requests for troubleshooting
* Avoid long-running synchronous work before sending the acknowledgment response

A common pattern is to validate and enqueue the event first, return `200 OK`, and then process it asynchronously in your own system.

### Example Event Handling Flow

1. BrickVerse sends an event to your webhook URL
2. Your server reads and validates the payload
3. Your server stores or queues the event for processing
4. Your server responds with:
   * Status: `200`
   * Body: `OK`
5. Your background systems handle the event logic

### Example Response

Your webhook handler should return something equivalent to:

```
HTTP/1.1 200 OK
Content-Type: text/plain

OK
```

### Example Use Cases

#### `user.deleted`

You may want to use this event to:

* remove user-related cached data
* delete external profile records
* anonymize analytics or stored identifiers
* comply with your own privacy workflows

#### `user.moderated`

You may want to use this event to:

* sync bans to external community systems
* revoke access to linked services
* restore access when a user is unbanned
* record moderation activity for auditing

### Important Notes

* Webhook deliveries may be retried, so your system should be prepared to receive the same event more than once
* Your endpoint should not rely on exact retry timing
* Failure to consistently acknowledge deliveries may result in webhook removal after repeated failures
