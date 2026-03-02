# OpenID OAuth

This guide explains how to:

* Register an OAuth app
* Implement Authorization Code Flow (with optional PKCE)
* Exchange tokens
* Retrieve user data with OpenID Connect
* Manage user authorizations

***

### 🌐 Base URLs

* **API Base:**\
  `https://api.brickverse.gg`
* **Versioned Prefix:**\
  `/api/v3`

Example full endpoint:

```
https://api.brickverse.gg/api/v3/oauth/token
```

***

## 🔐 Authentication Overview

BrickVerse OAuth supports:

| Auth Type                                       | Used For                      |
| ----------------------------------------------- | ----------------------------- |
| **Session Auth (cookie)**                       | App management + user consent |
| **Client Auth (`client_id` + `client_secret`)** | Token exchange                |
| **Bearer Token**                                | UserInfo endpoint             |

***

## 📦 Supported Scopes

When registering apps or requesting authorization, use these scope values:

* `OPENID`
* `PROFILE`
* `EMAIL`
* `PHONE`
* `GUILDS`

Example scope string:

```
OPENID PROFILE EMAIL
```

***

## 1️⃣ Register an OAuth Application

### Create an App

**Endpoint:**

```
POST /api/v3/oauth/apps
```

(Session authentication required)

#### Request Body

```json
{
  "name": "My App",
  "description": "My BrickVerse integration",
  "entryLink": "https://myapp.example.com",
  "tosUrl": "https://myapp.example.com/tos",
  "privacyUrl": "https://myapp.example.com/privacy",
  "scopes": ["OPENID", "PROFILE", "EMAIL"],
  "redirectUrls": ["https://myapp.example.com/oauth/callback"]
}
```

#### Response

Returns your app including:

* `clientId`
* `clientSecret`

⚠️ Store your `clientSecret` securely. Never expose it in frontend code.

***

### Manage Your Apps

| Method | Endpoint                        | Description             |
| ------ | ------------------------------- | ----------------------- |
| GET    | `/api/v3/oauth/apps`            | List your apps          |
| GET    | `/api/v3/oauth/apps/:id`        | Retrieve app details    |
| PUT    | `/api/v3/oauth/apps/:id`        | Update app (DRAFT only) |
| POST   | `/api/v3/oauth/apps/:id/submit` | Submit for approval     |
| DELETE | `/api/v3/oauth/apps/:id`        | Delete app (DRAFT only) |

Only approved apps can be used in production authorization flows.

***

## 2️⃣ Authorization Code Flow (with optional PKCE)

BrickVerse supports standard OAuth 2.0 + OpenID Connect.

***

### Step 1: Request Consent Data

```
GET /api/v3/oauth/authorize
```

(Session auth required)

#### Query Parameters

| Parameter               | Required | Notes                     |
| ----------------------- | -------- | ------------------------- |
| `client_id`             | ✅        | Your app’s ID             |
| `redirect_uri`          | ✅        | Must match registered URL |
| `response_type`         | ✅        | `code`                    |
| `scope`                 | ✅        | Space-separated           |
| `state`                 | Optional | CSRF protection           |
| `nonce`                 | Optional | Required for OpenID       |
| `code_challenge`        | Optional | For PKCE                  |
| `code_challenge_method` | Optional | `plain` or `S256`         |

#### Example

```
GET /api/v3/oauth/authorize?client_id=123&redirect_uri=https%3A%2F%2Fmyapp.example.com%2Foauth%2Fcallback&response_type=code&scope=OPENID%20PROFILE%20EMAIL&state=abc123&code_challenge=XYZ&code_challenge_method=S256
```

This returns consent screen data for your UI.

***

### Step 2: Submit Consent Decision

```
POST /api/v3/oauth/authorize
```

(Session auth required)

```json
{
  "client_id": "123",
  "redirect_uri": "https://myapp.example.com/oauth/callback",
  "scope": "OPENID PROFILE EMAIL",
  "state": "abc123",
  "consent": true,
  "nonce": "nonce-value",
  "code_challenge": "XYZ",
  "code_challenge_method": "S256"
}
```

#### Response

```json
{
  "redirect": "https://myapp.example.com/oauth/callback?code=AUTH_CODE&state=abc123"
}
```

If denied:

```
error=access_denied
```

***

## 3️⃣ Exchange Authorization Code for Tokens

```
POST /api/v3/oauth/token
```

Supported grant types:

* `authorization_code`
* `refresh_token`

***

### Authorization Code Exchange

```bash
curl -X POST "https://api.brickverse.gg/api/v3/oauth/token" \
  -H "Authorization: Basic BASE64(client_id:client_secret)" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "code": "AUTH_CODE",
    "redirect_uri": "https://myapp.example.com/oauth/callback",
    "code_verifier": "PKCE_VERIFIER_IF_USED"
  }'
```

#### Success Response

```json
{
  "access_token": "...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "...",
  "scope": "OPENID PROFILE EMAIL",
  "id_token": "..."
}
```

If `OPENID` scope was granted, an `id_token` will be returned.

***

### Refresh Token Exchange

```bash
curl -X POST "https://api.brickverse.gg/api/v3/oauth/token" \
  -H "Authorization: Basic BASE64(client_id:client_secret)" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "refresh_token",
    "refresh_token": "REFRESH_TOKEN"
  }'
```

***

## 4️⃣ Get User Information (OpenID Connect)

```
GET /api/v3/oauth/userinfo
```

```bash
curl "https://api.brickverse.gg/api/v3/oauth/userinfo" \
  -H "Authorization: Bearer ACCESS_TOKEN"
```

#### Response

Returns claims based on granted scopes.

Minimum claim:

```
sub
```

Additional claims depend on:

* `PROFILE`
* `EMAIL`
* `PHONE`
* `GUILDS`

***

## 5️⃣ Discovery & JWKS

BrickVerse provides OpenID Connect discovery:

* `GET /.well-known/openid-configuration`
* `GET /.well-known/jwks.json`

Use the discovery document to dynamically retrieve:

* Authorization endpoint
* Token endpoint
* UserInfo endpoint
* `jwks_uri`

***

## 6️⃣ User Authorized App Management

Users can manage connected applications.

| Method | Endpoint                            | Description         |
| ------ | ----------------------------------- | ------------------- |
| GET    | `/api/v3/oauth/authorized-apps`     | List connected apps |
| DELETE | `/api/v3/oauth/authorized-apps/:id` | Revoke access       |

Revoking deletes:

* Authorization
* Access tokens
* Refresh tokens

***

## ⚠️ Common Error Codes

#### Token Endpoint

* `invalid_client`
* `invalid_request`
* `invalid_grant`
* `unsupported_grant_type`

#### UserInfo Endpoint

* `invalid_token`

***

## ✅ Best Practices

* Always use HTTPS
* Use PKCE for public clients (SPA / mobile)
* Validate `state` and `nonce`
* Store secrets securely
* Implement token refresh logic
* Validate `id_token` signature using JWKS
