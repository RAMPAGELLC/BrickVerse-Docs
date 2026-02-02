# What's Authority?

### What Is Script Authority?

**Script authority** determines what a script in your world is allowed to do — especially when it comes to **reading** or **modifying data**. Higher authority levels grant more control, while lower levels are more restricted to protect security.

### How Are ModuleScripts Classified?

ModuleScripts are assigned an **authority level** based on **where they are executed**.

* **Called from the client** → **Authority Level 1**
* **Called from the server** → **Authority Level 2**

This distinction helps us determine how much trust and access a script should have within the system.

***

### Authority Levels Explained

#### **Level 1 — Client**

Used for scripts that run on a player’s device. These have the lowest level of trust and cannot access or modify protected server systems.

#### **Level 2 — Server**

Used for scripts running on the server. These are more trusted and can interact with secure systems that are completely inaccessible to client-side scripts.

{% hint style="danger" %}
**Important:** Authority Levels **2 and higher** are fully protected from client access. Clients cannot read, modify, or interfere with these scripts.
{% endhint %}

***

#### **Level 4 — Core**

This level is reserved for **core internal systems**.

* Can **read** certain protected data
* **Cannot modify** that data unless explicitly permitted by another Level 4 system
* Designed for sensitive internal logic that needs visibility but limited write power

***

#### **Level 5 — Backend**

This is the **highest authority level** and is used for **backend services and APIs**.

* Can **assign authority levels** to other systems
* Its data **cannot be read or modified** by Level 4 or lower
* Reserved strictly for secure backend infrastructure

***

### Summary

| Level | Name    | Typical Use                         | Can Be Accessed by Client? |
| ----- | ------- | ----------------------------------- | -------------------------- |
| 1     | Client  | Player-side logic                   | Yes (runs locally)         |
| 2     | Server  | Game server logic                   | ❌ No                       |
| 4     | Core    | Internal systems (like Leaderboard) | ❌ No                       |
| 5     | Backend | APIs & services                     | ❌ No                       |
