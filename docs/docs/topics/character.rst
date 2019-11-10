.. _character:

Character
=========

Gamma provides :api:`gma.character`, which is a convenience class for
representing an **entity controlled by the player**.
In most games there is only one such entity (multiple in multiplayer games)
and it is called the character.

The :api:`gma.character` class extends :api:`gma.moveable` and provides some
extra functions for changing the state of the entity -- to control jumping and
moving.

.. note:: See :ref:`moveables` for what else is provided for the character


Instantiating the character
---------------------------

The character is a :api:`moveable entity <gma.moveable>`, which in turn is a
:api:`rectangle <gma.shapes.rectangle>`. Therefore you should provide the
dimensions and position when specifying a character.

The character is typically instantiated and provided to the manager. For example:

.. code-block:: javascript

    var manager = gma.manager(...);
    manager.character = gma.character({
        left     : 0,
        bottom   : 0,
        width    : 3,
        height   : 6,
        depth    : 3
    });

See the :ref:`shapes <rectangle>` topic for possible combinations of dimensions
and position.

.. note:: The position properties of a character is ignored
    (:ref:`spawn points <spawnPoints>` are defined per level) but is still
    required.


Jumping
-------

The :metho:`gma.character.jump` method is used to tell the character to jump.
It sets the character's ``ystate`` to :constant:`JUMPING` when the character
isn't already jumping and sets it's ``velocity`` to what has been defined for
it's ``jumpVelocity`` property.

The jump function is designed to be bound to a key-press:

.. code-block:: javascript

    // Jump when spacebar (keycode 32) is pressed
    gma.keyHandler.register(32, manager.character.jump);

.. note:: If the character is dead (character's :prop:`gma.character.alive`
    property isn't set to ``true``) :metho:`gma.character.jump` will have no
    effect.

Moving
------

To tell the character to move left or right, the :metho:`gma.character.move`
method is supplied. This function accepts one of the :api:`gma.constants`
to specify the direction we want to move in (either :constant:`LEFT` or
:constant:`RIGHT`) and an event object.

It will then set :prop:`gma.character.xState` on the character to this direction
if the event object is a ``keydown``, otherwise it will set the character's
:prop:`gma.character.xState` to :constant:`STILL` if the event is a ``keyup``.

An example keybinding would be (with or without :term:`currying <curry>`):

.. code-block:: javascript

    // Using currying
    gma.keyHandler.register(39, manager.character.move.curry(gma.constants.RIGHT));
    gma.keyHandler.register(37, manager.character.move.curry(gma.constants.LEFT));

    // Not using currying
    gma.keyHandler.register(39, function(e) {
        manager.character.move(gma.constants.RIGHT, e);
    });
    gma.keyHandler.register(37, function(e) {
        manager.character.move(gma.constants.LEFT, e);
    });

.. note:: If the character is dead (character's :prop:`gma.character.alive`
    property isn't set to ``true``) :metho:`gma.character.move` will have no
    effect.


Collision functionality
-----------------------

The :api:`gma.character` class defines additional collision functionality.
After doing the collision checks it inherits, the
:api:`character <gma.character>` check if it collided with a
:api:`gma.collectable` and calls :metho:`gma.collectable.pickup` on the
collectable and increment :prop:`gma.character.score` on the character.

.. note:: This is implemented in the
    :metho:`gma.character.collided__pickupCollectable` function.
    See the advanced topic on
    :ref:`collision functionality <collisionFunctions>` to find out how to
    customize collision behaviours.
