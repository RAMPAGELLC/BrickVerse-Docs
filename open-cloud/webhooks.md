# Webhooks

### Introduction

BrickVerse.gg provides a powerful webhook system that allows you to receive real-time notifications about various events occurring on your platform.&#x20;

One of the events supported by BrickVerse.gg Webhooks is the "RightToErasure" event, which is designed to facilitate the automated erasure of database information pertaining to a user. This document outlines the details of the BrickVerse.gg Webhooks for the "RightToErasure" event, along with an example of how to set up and use webhooks in JavaScript using the NPM package "**brickverse**".

#### Prerequisites

Before implementing BrickVerse.gg Webhooks for the "RightToErasure", or other events, make sure you have the following prerequisites in place:

1. A BrickVerse.gg account: You need an account on BrickVerse.gg to access the webhook system.
2. API Keys: Obtain your API keys from BrickVerse.gg, which will be used to authenticate your webhook requests.
3. Node.js and NPM: Ensure you have Node.js and NPM installed on your development environment.
4. NPM Package: Install the "**brickverse**" NPM package to work with BrickVerse.gg webhooks.

### RightToErasure Event Example

The "**RightToErasure**" event is a specific webhook event provided by BrickVerse.gg. This event is designed to help you set up an automated process for erasing user-related data from your database. When this event is triggered, BrickVerse.gg will send a payload containing relevant information about the erasure request. Here is an example of the "**RightToErasure**" event payload:

```json
{
    "EventId": "XXXX-XXXX-XXXX-XXXX",
    "Event": "RightToErasure",
    "EventTime": "2023-12-30T16:24:24.2118874Z", // Type: ISO 8601 Timestamp
    "EventPayload": {
        "World": 1, // World ID for erasure
        "UserId": 2, // User ID for erasure
    }
}
```

* `EventId`: A unique identifier for the event.
* `Event`: Indicates that this event is a "RightToErasure" event.
* `EventTime`: The timestamp when the event was triggered in ISO 8601 format.
* `EventPayload`: Contains specific information related to the erasure request, such as the "World" and "UserId."

### Using BrickVerse.gg Webhooks with NPM Package "brickverse"

To receive and handle "**RightToErasure**" events from BrickVerse.gg, you can use the NPM package "**brickverse**." Here's an example of how to set up a webhook handler in JavaScript using this package:

#### Installation

First, install the "brickverse" package using NPM:

```bash
npm install brickverse
```

#### Example Code

```javascript
const { Client, OpenCloudClient } = require('brickverse');

// Define your API credentials
const apiKey = 'your-api-key';
const apiSecret = 'your-api-secret';

// Initialize the BrickVerse client
const OpenCloud = new OpenCloudClient(apiKey, apiSecret);

// Define a handler for the RightToErasure event
OpenCloud.Webhooks.on('RightToErasure', (payload) => {
    console.log('Received RightToErasure event: ', payload);
    
    // Implement your erasure logic here
});
```

In the code above, you need to replace `'your-api-key'` and `'your-api-secret'` with your actual API credentials provided by BrickVerse.gg.&#x20;

The example code sets up a webhook handler for the "**RightToErasure**" event and listens for incoming events. When a "**RightToErasure**" event is received, it logs the payload and allows you to implement your custom erasure logic.

## Events

### RightToErasure

**Overview**

Handle right-to-erasure of data.

**Payload**

```json
{
    "EventPayload": {
        "World": 1, // World ID for erasure
        "UserId": 2, // User ID for erasure
    }
}
```

