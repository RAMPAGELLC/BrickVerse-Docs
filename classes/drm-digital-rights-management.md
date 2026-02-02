# DRM - Digital Rights Management

Brickverse provides built-in **Digital Rights Management (DRM)** controls to help creators and guilds decide how their assets can be accessed, shared, and used across the platform.

DRM settings are applied to supported assets such as **textures, logos, decals, audio, and other uploaded media**.

There are two privacy levels:

* **Public**
* **Ownership**

Each setting changes **who can access the file** and **how it is delivered** behind the scenes.

***

### 🔓 Public Assets

**Public** is the most open setting.

When an asset is set to Public:

* Anyone on Brickverse can **use it** where asset usage is allowed
* The file can be **downloaded and cached** through Brickverse’s global CDN
* It is treated as **community-available content**
* No special permissions are required to view or fetch the file

#### How it works technically

Public assets are:

* Stored in a **publicly accessible delivery layer**
* Distributed via our **Content Delivery Network (CDN)** for fast global loading
* Optimized for **performance and broad reuse**

#### When to use Public

Public is ideal for:

* Guild branding meant to be shared widely
* Community resources
* Free-to-use textures or media
* Promotional or open assets

{% hint style="warning" %}
**Important:** Public assets may be reused by others within platform rules. Only upload content you’re comfortable sharing broadly.
{% endhint %}

***

### 🔒 Ownership Assets

**Ownership** is the restricted, private setting.

When an asset is set to Ownership:

* It is **not publicly downloadable**
* It is stored in a **private bucket**
* Access is limited to:
  * The **asset owner**, or
  * Users with **edit permissions** in the **guild that owns the asset**

If someone does not meet those permission requirements, the asset file cannot be accessed directly.

#### How it works technically

Ownership assets are:

* Stored in **private cloud storage**
* Delivered using **secure, time-limited access**
* Protected from public scraping or direct CDN downloads
* Checked against **guild role permissions** before access is granted

#### When to use Ownership

Ownership is best for:

* Internal guild development assets
* Unreleased or work-in-progress content
* Paid, exclusive, or restricted-use resources
* Sensitive branding files

This setting ensures your content stays **within your team**.

***

### 👥 Permission Rules (Ownership Mode)

A user can access an Ownership asset only if **one** of the following is true:

1. They are the **original owner/uploader**, or
2. They belong to the owning **guild** **and** have a role with **edit permissions**

Regular guild members **without edit rights** cannot directly access or download these files.

***

### 🔄 Changing an Asset’s DRM Setting

If you have permission to manage an asset, you can:

1. Go to the asset’s management page
2. Open **Privacy / DRM Settings**
3. Choose **Public** or **Ownership**
4. Save changes

Changes may take a short time to propagate across our storage and delivery systems.

***

### 🧠 Choosing the Right Setting

| Goal                            | Recommended Setting |
| ------------------------------- | ------------------- |
| Share with the entire community | **Public**          |
| Keep within your guild team     | **Ownership**       |
| Distribute a free resource      | **Public**          |
| Protect unreleased content      | **Ownership**       |
| Internal branding drafts        | **Ownership**       |

***

### ❓ FAQ

**Q: Can Ownership assets ever be accessed publicly?**\
No. They are stored in private infrastructure and require proper authentication and permissions.

**Q: Does Public mean anyone can claim ownership of my asset?**\
No. Public affects **access**, not **ownership records**. You still remain the recorded creator/uploader.

**Q: Can I switch from Public to Ownership later?**\
Yes, but any previously downloaded copies outside Brickverse cannot be revoked.

**Q: Does Ownership affect in-game or in-platform usage?**\
No — if a system feature allows the asset and the user has permission, it will still function normally. DRM only controls **file-level access**.

***

### 📢 How Brickverse Displays Guild & World Branding

To ensure branding and promotional visuals display reliably across the platform, Brickverse may internally reprocess certain submitted media.

This includes:

* Guild logos
* Guild banners
* World thumbnails
* World icons
* Ad creatives

***

#### What happens behind the scenes

When these assets are used in **platform-wide surfaces** (such as discovery pages, featured sections, search results, or promotional slots), we:

* Create an **internal Developer Asset**
* Store that copy under the **Public** privacy setting
* Deliver it through our **global CDN**

This allows these visuals to be:

* Visible to **all users**, including visitors who are not logged in
* Loaded quickly and reliably across all Brickverse surfaces

***

#### 🤖 Why we re-upload internally

In addition to performance and visibility, this process allows us to run these assets through our **existing AI moderation subsystems**.

By standardizing logos, banners, thumbnails, and icons as internal Developer Assets, we can:

* Apply **automated safety and policy checks**
* Detect prohibited or restricted imagery
* Maintain consistent enforcement across all public-facing visuals
* Quickly review or take action if an asset is later reported

This helps us keep platform-wide promotional and branding areas **safe, compliant, and consistent.**&#x20;

***

### 🌳 World Trees (Game Source Files)

World Trees — the **source files for games** (similar to a `.rbxm/rbxmx`-style project file) — are always treated as **sensitive developer content** and are protected with the highest level of storage security on Brickverse.

These files contain the **full editable structure of a game**, including:

* Scripts and game logic
* Asset references
* World structure and configuration
* Systems that should never be exposed to players

Because of this, World Trees are **never stored as Public assets**.

***

#### 🔒 How World Trees Are Secured

All World Tree files are stored in a **private storage bucket** with strict access controls.

They can only be accessed by:

* Users with **edit permissions** for the game
* **Authenticated Brickverse game servers** that are authorized to load the experience

They are **not accessible** to:

* Regular players
* Game clients
* Users without edit-level permissions
* Public CDN endpoints

***

#### 🖥 Server-Only Access

When a game runs on Brickverse:

* The **server** securely fetches necessary game data
* The **client (player)** only receives replicated data required to play.
  * Instances like server scripts do not replicate.

This prevents users from extracting:

* Proprietary scripts
* Backend logic
* Anti-cheat systems
* Unreleased or hidden features

In other words, players can **play the game**, but they cannot download the **source project file**.

***

#### 👥 Permission Rules

A user can download or edit a World Tree only if they:

1. Are the **game owner**, or
2. Have a role with **edit permissions** on that specific game.

####

