# AdService

This AdService class was historically a service used to display mobile video ads as a form of game monetization. This service requires approval of videos ads through our system.\
\
AdService is strictly only allowed usage for Android & iOS players.\
\
Limit of 2 ads per 30 minutes per user.

### Benefits <a href="#benefits" id="benefits"></a>

Implementing video ad impressions in mobile gameplay sessions offers a variety of positive things for BrickVerse developers.

The more hits your ad got, the more Cubes you earned (at a rate of one Cubes per 20 impressions). So if you were trying to utilize the heavy traffic you received in your game, it was recommended to using the API to call the commercial before your game started. For those who already had a hit game, this this could have functioned as supplemental income.

## Properties

|                                                            |                 |
| ---------------------------------------------------------- | --------------- |
| `boolean` Enabled <mark style="color:red;">`Locked`</mark> | false (Default) |

## Functions

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| `void` RequestAdService(**String** AdKey, **Table** Limits)                                         |
| Requests Ad Object for your Universe.                                                               |
| `void` DisplayAd(**RequestAdService Instance** Object, **Player Object** Player, **number** Amount) |
| Displays add with Ad Object towards Player with amount of ads to display                            |
| `void` CanDisplayAd(**Player Object** Player)                                                       |
| Returns boolean if ads can be displayed or not to the player                                        |
