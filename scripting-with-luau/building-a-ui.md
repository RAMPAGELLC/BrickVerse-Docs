# Building a UI

BrickVerse interfaces use Instances. The local player's UI hierarchy is available through the global `PlayerGUI`.

UI should normally be created and controlled by a `ClientScript`.

## Basic UI hierarchy

```text
PlayerGUI
└── UIContainer
    ├── UILabel
    └── UIButton
```

## Create a panel

```lua
local panel = Instance.New("UIContainer", PlayerGUI)
panel.Name = "MainPanel"
panel.PositionRelative = Vector2.New(0.5, 0.5)
panel.PositionOffset = Vector2.New(-200, -120)
panel.SizeOffset = Vector2.New(400, 240)
panel.Visible = true
```

`PositionRelative` places the object relative to the parent. `PositionOffset` applies a pixel-like offset.

## Add a background

`UIContainer` handles layout and clipping. Add a `UIView` for a visible background:

```lua
local background = Instance.New("UIView", panel)
background.Name = "Background"
background.SizeRelative = Vector2.One
background.Color = Color.FromHex("#1A2433")
background.BorderColor = Color.FromHex("#2D3C52")
background.BorderWidth = 1
background.CornerRadius = 12
```

## Add a label

```lua
local title = Instance.New("UILabel", panel)
title.Name = "Title"
title.PositionOffset = Vector2.New(24, 20)
title.SizeOffset = Vector2.New(352, 48)
title.Text = "Welcome to BrickVerse"
title.TextColor = Color.FromRGB(255, 255, 255)
title.FontSize = 24
title.HorizontalAlignment = HorizontalAlignment.Center
title.VerticalAlignment = VerticalAlignment.Middle
title.TextWrapped = true
```

## Add a button

```lua
local button = Instance.New("UIButton", panel)
button.Name = "ContinueButton"
button.PositionOffset = Vector2.New(100, 160)
button.SizeOffset = Vector2.New(200, 48)
button.Text = "Continue"
button.Color = Color.FromRGB(1, 135, 248)
button.TextColor = Color.FromRGB(255, 255, 255)
button.FontSize = 18
button.CornerRadius = 8
```

Listen for a click:

```lua
button.Clicked:Connect(function()
	print("Continue clicked")
	panel.Visible = false
end)
```

## Hover effects

```lua
local normalColor = Color.FromRGB(1, 135, 248)
local hoverColor = Color.FromRGB(30, 155, 255)

button.MouseEnter:Connect(function()
	button.Color = hoverColor
end)

button.MouseExit:Connect(function()
	button.Color = normalColor
end)
```

## Text input

```lua
local input = Instance.New("UITextInput", panel)
input.Name = "NameInput"
input.PositionOffset = Vector2.New(50, 90)
input.SizeOffset = Vector2.New(300, 44)
input.Placeholder = "Enter a name"
input.TextColor = Color.FromRGB(255, 255, 255)
input.PlaceholderColor = Color.FromRGB(150, 160, 175)
input.Color = Color.FromHex("#111923")
input.FontSize = 17
input.MultiLine = false
```

React to changes:

```lua
input.Changed:Connect(function(value)
	print("Current text:", value)
end)

input.Submitted:Connect(function(value)
	print("Submitted:", value)
end)
```

Focus the field:

```lua
input:Focus()
```

## Images

```lua
local image = Instance.New("UIImage", panel)
image.Name = "Avatar"
image.PositionOffset = Vector2.New(20, 80)
image.SizeOffset = Vector2.New(64, 64)
image.ImageType = ImageType.UserAvatarHeadshot
image.ImageID = Players.LocalPlayer.UserID
```

## Scrolling content

```lua
local scroll = Instance.New("UIScrollView", PlayerGUI)
scroll.Name = "InventoryScroll"
scroll.PositionOffset = Vector2.New(20, 20)
scroll.SizeOffset = Vector2.New(320, 480)
scroll.VerticalScrollMode = UIScrollMode.Auto
scroll.HorizontalScrollMode = UIScrollMode.Disabled
```

Add a layout:

```lua
local layout = Instance.New("UIVLayout", scroll)
layout.Name = "Layout"
```

Then parent item rows to the layout or scroll hierarchy according to your interface structure.

## Grid layout

```lua
local grid = Instance.New("UIGridLayout", scroll)
grid.Name = "ItemGrid"
grid.Columns = 4
grid.Spacing = 8
```

## Z-index and clipping

```lua
panel.ZIndex = 10
panel.ClipDescendants = true
```

Higher `ZIndex` values render above lower values.

## Absolute size

Read calculated layout values:

```lua
print(panel.AbsolutePosition)
print(panel.AbsoluteSize)
```

These values are read-only.

## Updating a HUD

```lua
local scoreLabel = Instance.New("UILabel", PlayerGUI)
scoreLabel.Name = "Score"
scoreLabel.PositionOffset = Vector2.New(24, 24)
scoreLabel.SizeOffset = Vector2.New(240, 40)
scoreLabel.TextColor = Color.FromRGB(255, 255, 255)
scoreLabel.FontSize = 20
scoreLabel.HorizontalAlignment = HorizontalAlignment.Left

local function setScore(score: number)
	scoreLabel.Text = "Score: " .. tostring(score)
end

setScore(0)
```

A client should display an authoritative score received from the server. It should not decide the score itself.

## Complete menu example

```lua
local panel = Instance.New("UIView", PlayerGUI)
panel.Name = "WelcomePanel"
panel.PositionRelative = Vector2.New(0.5, 0.5)
panel.PositionOffset = Vector2.New(-220, -140)
panel.SizeOffset = Vector2.New(440, 280)
panel.Color = Color.FromHex("#1A2433")
panel.BorderColor = Color.FromHex("#30425B")
panel.BorderWidth = 1
panel.CornerRadius = 14

local title = Instance.New("UILabel", panel)
title.Name = "Title"
title.PositionOffset = Vector2.New(30, 30)
title.SizeOffset = Vector2.New(380, 60)
title.Text = "BrickVerse"
title.TextColor = Color.FromRGB(255, 255, 255)
title.FontSize = 30
title.HorizontalAlignment = HorizontalAlignment.Center

local description = Instance.New("UILabel", panel)
description.Name = "Description"
description.PositionOffset = Vector2.New(40, 100)
description.SizeOffset = Vector2.New(360, 60)
description.Text = "Build, explore, and play together."
description.TextColor = Color.FromRGB(205, 215, 228)
description.FontSize = 17
description.TextWrapped = true
description.HorizontalAlignment = HorizontalAlignment.Center

local playButton = Instance.New("UIButton", panel)
playButton.Name = "Play"
playButton.PositionOffset = Vector2.New(120, 190)
playButton.SizeOffset = Vector2.New(200, 52)
playButton.Text = "Play"
playButton.Color = Color.FromRGB(1, 135, 248)
playButton.TextColor = Color.FromRGB(255, 255, 255)
playButton.FontSize = 19
playButton.CornerRadius = 9

playButton.Clicked:Connect(function()
	panel.Visible = false
end)
```
