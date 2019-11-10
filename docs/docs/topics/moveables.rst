.. _moveables:

Moveable Entities
=================

Gamma has abstracted the functionality required to a move an entity into the
:api:`gma.moveable` class. This class is currently used by :api:`gma.character`
and :api:`gma.enemy`.

This class provides properties that represent the movement state of an entity
as well as functions for changing these states and functions for updating the
entity's position.

Representing an entities' state
-------------------------------

Although Gamma is rendered in 3D all entities move in 2D. As a result of this,
the movement state only needs to keep track of the entities' horizontal and vertical movement.

Horizontal State
++++++++++++++++

The horizontal state of an entity is held in it's :prop:`gma.moveable.xState`
property. Gamma provides :constant:`STILL`, :constant:`RIGHT` and
:constant:`LEFT` as valid values for this property.

For convenience, :api:`gma.moveable` also provides
:prop:`gma.moveable.lastXState`, which is used to determine what direction the
entity was going in before it stopped moving.

.. note:: :prop:`gma.moveable.lastXState` can also be used to set the direction
    an entity is looking in when it is first created, due to it's use in
    :metho:`gma.moveable.getRotation`.

Vertical State
++++++++++++++

The vertical state of an entity is held in it's :prop:`gma.moveable.yState`
property. Gamma provides :constant:`STILL`, :constant:`JUMPING` and
:constant:`FALLING` as valid values for this property.

When an entity starts jumping, it will use :prop:`gma.moveable.jumpVelocity` to
determine what vertical velocity the entity should start with. For the rest of
the time the entity is in the air, it's vertical velocity is held by
:prop:`gma.moveable.velocity`, which is changed by
:metho:`gma.moveable.getMovement`.

Changing an entities' direction
-------------------------------

Changing an entities' movement state is not controlled by :api:`gma.moveable`.
Rather, it is the responsibility of each class that subclasses
:api:`gma.moveable`.

For example, :api:`gma.character` provides the functions
:metho:`gma.character.move` and :metho:`gma.character.jump` which when called
through combination with :api:`keybindings <gma.keyHandler>` will change the
entities movement states and allow the player to control the entity.

On the other  hand, :api:`gma.enemy` entities override
:metho:`gma.moveable.getMovement` such that the movement state of the entity
is determined every time :metho:`gma.moveable.animate` is called.

Updating an entities` position
-------------------------------

To change the position of an entity according to it’s vertical and horizontal
state, :api:`gma.moveable` provides :metho:`gma.moveable.animate` and
:metho:`gma.moveable.getMovement`.  The :metho:`gma.moveable.getMovement`
function returns a movement vector calculated from the entity’s current vertical
and horizontal state and is used by the :metho:`gma.moveable.animate` function,
which in turn, is called as part of the Game Loop.

The animate function does the following:

* Determine a movement vector
* Use :metho:`gma.collisions.detectCollisions` to determine how far the entity
  can move along this movement vector.
* Change the position of the entity using :metho:`gma.moveable.updatePositions`.
* Determine if the entity is on standing on top of something by calling
  :metho:`gma.moveable.findGround` and change the vertical state of the entity
  to :constant:`FALLING` or :constant:`STILL` as appropriate.

.. note:: :metho:`gma.collisions.detectCollisions` will only be used if either
    :prop:`gma.moveable.xState` or :prop:`gma.moveable.yState` are not
    :constant:`STILL`, but :metho:`gma.moveable.updatePositions` and
    :metho:`gma.moveable.findGround` will always be called.

Utility functions
-----------------

There are a couple of other functions that :api:`gma.moveable` provides,
:metho:`gma.moveable.getRotation` and :metho:`gma.moveable.kill`.

The :metho:`gma.moveable.kill` method will set :prop:`gma.moveable.alive` to
false and set :prop:`gma.moveable.xState` to :constant:`STILL`.
This ensures the entity won't continue moving after being "killed", and
:metho:`gma.manager.removeDead` will become aware that this entity should
be removed.

The :metho:`gma.moveable.getRotation` is purely for changing the visual
representation of an entity. When called, it will look at the state of the
entity and determine which direction it should be facing and return a number
representing how far around the y-axis the entity should be rotated.
