# Frame

Frame is a `UIObject` that renders as a plain rectangle with no other content. They are the simplest concrete example of a [`UIObject`](broken-reference), as they provide very little additional functionality (`Frame.FrameStyle`). Despite this, Frames are useful as containers for other [`UIObject`](broken-reference)s, such as [`TextLabel`](textlabel.md), [`ImageLabel`](imagelabel.md). The key benefit to using a Frame over a [`Folder`](broken-reference) as a container object is the ability to further manipulate the `GuiObject.Size` and `GuiObject.Position` of any descendants.
