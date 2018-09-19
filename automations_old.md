# Automations

* [Arriving Home](#arriving-home)
* [Leaving](#leaving)
* [Back Door Opens](#back-door-opens)
* [Goodnight Switch](#goodnight-switch)
* [Wake Up Light Slowly at 630AM](#wake-up-light-slowly-at-630am)
* [Send picture when all devices change state](#send-picture-when-all-devices-change-state)

### Arriving Home

#### Triggers
* `group.all_devices` state changes from away to home
#### Conditions
* Not during night mode and away mode is active
#### Actions
* Activate the SmartThings routine I'm Home

---
### Leaving

#### Triggers
* `group.all_devices` state changes from home to away
#### Conditions
* Away mode is already off
* Night mode is not active
#### Actions
* turn on SmartThings routine Empty Home
----
### Back Door Opens

#### Triggers
* Back door opens
#### Conditions
* Away mode is active
* Night mode is not active
#### Actions
* Turn on the SmartThings routine "Back Door Opens"
* Make a persistent notification saying "Back door intrusion detected"

---

### Goodnight Switch

#### Triggers
* When the switch "VD_Routine_Goodnight" is turned on

#### Actions
* Turn on the `goodnight_switch` script

---

### Wake Up Light Slowly at 630AM

#### Triggers
* At 6:30AM 
#### Conditions
* Home mode is "night"
* on the weekday
#### Actions
* run the python script to slowly fade in the master bedroom lights to 50%
---

### Send picture when all devices change state
#### Triggers
* when `group.all_devices` change state

#### Actions
* Send a snapshot of the Raspberry Pi camera to Adam's phone via HTML5
