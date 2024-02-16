---
description: Camera Services for your world. Making everything possible!
---

# Camera

### Where the Camera object is found <a href="#where-the-camera-object-is-found" id="where-the-camera-object-is-found"></a>

In an instance of the game, each client has its own Camera object associated with it. Camera objects exist only upon the viewer’s client, residing in that user’s local Workspace, and therefore cannot be edited directly from the server.

Each client’s particular Camera object can be accessed through the `Workplace.CurrentCamera` property of the [`Workplace`](../serviceprovider/workplace-1.md) on that client.



### How the Camera object works <a href="#how-the-camera-object-works" id="how-the-camera-object-works"></a>

The Camera’s properties define the current view of the 3D game world. The most important of these being:

* The `Camera.CFrame` property represents the position and orientation of the camera.
* The `Camera.Focus` property represents the point the camera is looking at. It is important this property is set as it also represents where the game thinks you are in the world. Certain visuals will be more detailed and will update more frequently, depending on how close they are to the Focus. BrickVerse's default camera scripts take care of this.
* The `Camera.CameraType` property is read by the game’s camera scripts and determines how the Camera should update each frame.
* The `Camera.CameraSubject` property is read by the game’s camera scripts and determines what object the Camera should follow.
* The `Camera.FieldOfView` property represents the extent of the observable world visible.

## Properties

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set
