# Beautiful JSON Display

On API requests add Query Param "BV\_ENV\_SEXY\_JSON" for JSON responses to display opened and nice.

## Example

### Without

```json
{"status":"ok","message":"OpenCloud API v2 Version information located.","version":"3c0c7137a3424cb4d8ba0bb1d751cfc4-vq9oisbetterdev","log":{"version":"3c0c7137a3424cb4d8ba0bb1d751cfc4-vq9oisbetterdev","title":"What's new","art":"https:\/\/cdn.brickverse.gg\/img\/art\/intro.png","published":"Published on November 28, 2023","body":"Make sure to join our community discord, we are still working daily on new features.","headlines":[{"headline":"SITE","changes":["Speed improvements.","New payment proccesser completed.","Currency purchase amount has been lowered, they still maintain the same valuation","Other misc fixes."]},{"headline":"ENGINE","changes":["BrickLua API.","Backend Draft."]}],"previous_version":"3c0c7137a3424cb4d8ba0bb1d751cfc4-franyisgooddev69","previous":{"version":"3c0c7137a3424cb4d8ba0bb1d751cfc4-franyisgooddev69","title":"What's new","art":"https:\/\/cdn.brickverse.gg\/img\/art\/intro.png","published":"Published on November 26, 2023","body":"Make sure to join our community discord.","headlines":[{"headline":"SITE","changes":["New changes modal","Site security improvements","Speed improvements"]},{"headline":"ENGINE","changes":["BrickLua API","Backend Draft"]}]}}}
```

### With

```json
{
    "status": "ok",
    "message": "OpenCloud API v2 Version information located.",
    "version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-vq9oisbetterdev",
    "log": {
        "version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-vq9oisbetterdev",
        "title": "What's new",
        "art": "https:\/\/cdn.brickverse.gg\/img\/art\/intro.png",
        "published": "Published on November 28, 2023",
        "body": "Make sure to join our community discord, we are still working daily on new features.",
        "headlines": [
            {
                "headline": "SITE",
                "changes": [
                    "Speed improvements.",
                    "New payment proccesser completed.",
                    "Currency purchase amount has been lowered, they still maintain the same valuation",
                    "Other misc fixes."
                ]
            },
            {
                "headline": "ENGINE",
                "changes": [
                    "BrickLua API.",
                    "Backend Draft."
                ]
            }
        ],
        "previous_version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-franyisgooddev69",
        "previous": {
            "version": "3c0c7137a3424cb4d8ba0bb1d751cfc4-franyisgooddev69",
            "title": "What's new",
            "art": "https:\/\/cdn.brickverse.gg\/img\/art\/intro.png",
            "published": "Published on November 26, 2023",
            "body": "Make sure to join our community discord.",
            "headlines": [
                {
                    "headline": "SITE",
                    "changes": [
                        "New changes modal",
                        "Site security improvements",
                        "Speed improvements"
                    ]
                },
                {
                    "headline": "ENGINE",
                    "changes": [
                        "BrickLua API",
                        "Backend Draft"
                    ]
                }
            ]
        }
    }
}
```
