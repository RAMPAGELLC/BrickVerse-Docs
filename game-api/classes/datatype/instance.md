# Instance

{% hint style="warning" %}
**NotCreatable**

This object cannot be created with the [`Instance.new`](/broken/pages/N8HYF3qH4Rt1G5EZKSLY) constructor function.
{% endhint %}

Instance is the base class for all classes in the BrickVerse class hierarchy. Every other class that the BrickVerse engine defines inherits all of the members of Instance. It is not possible to directly create Instance objects.

Instance has a special function called `Instance.new` which is used to create objects via code. This function takes the name of the class as a parameter and returns the created object. Abstract classes and services cannot be created with the `Instance.new` function.

Inherited from [Dynamic](https://developers.brickverse.gg/game-api/classes/dymanic) Set
