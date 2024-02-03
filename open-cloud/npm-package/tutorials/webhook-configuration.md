# Webhook Configuration

You may see something similar in your console saying:

```
OpenCloudClient server is listening on port ${port}. Live URL: ${url}. Setup Instructions: 
```

Copy the Live URL it spits out, it should look something similar to this:

<pre><code><strong>http://ipv4:port/bvnpm/webhook
</strong></code></pre>

Make sure the IPv4 is NOT a local/private IP like 127.0.0.1 or 192.168.0.0,

Go to BrickVerse Account Settings:

{% embed url="https://www.brickverse.gg/my/settings" %}

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Select OpenCloud

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

Enter the webhook live URL and press create.

## Congrats your webhook is now live!

## Handling webhook events

[https://developers.brickverse.gg/open-cloud/webhooks](https://developers.brickverse.gg/open-cloud/webhooks)
