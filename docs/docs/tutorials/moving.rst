Make the character move
=======================

To make the character move, we have to tell Gamma to change the horizontal
and/or vertical state of the character when a particular key is pressed.
For this tutorial, we'll make it so:

* pressing left arrow makes the character go left
* pressing right arrow makes the character go right
* pressing spacebar makes the character jump

KeyCodes
--------

First we need to know the corresponding number for these buttons. If we look
this :ref:`list of keycodes <keycodes>` we can see that the left arrow is 37,
right arrow is 39, and spacebar is 32.

Functions to move the character
-------------------------------

Next we need to know which functions must be called to `change the state` of the
character. After telling the character that it is moving right, the game loop
then causes the character to be moved at a constant rate.

We will call :metho:`gma.character.move` and :metho:`gma.character.jump` to
change the state of the character. To go left, we need to call
:metho:`gma.character.move` with :constant:`LEFT` as an argument.
Going right is the same, except using :constant:`RIGHT` as the argument.
Jumping just requires calling :metho:`gma.character.jump`.
Both of these functions (:metho:`gma.character.move` and
:metho:`gma.character.jump`) also require the key press event object as an
argument.

We use :metho:`gma.keyHandler.register` to register a function to a particular
key press. This function will be called with the keyboard event, which is used
to differentiate between pressing and releasing a key.

.. code-block:: javascript

    gma.keyHandler.register(37, function (keyEvent) {
        manager.character.move(gma.constants.LEFT, keyEvent);
    });

    gma.keyHandler.register(39, function (keyEvent) {
        manager.character.move(gma.constants.RIGHT, keyEvent);
    });

    gma.keyHandler.register(32, manager.character.jump);

Key binding is provided by :api:`gma.keyHandler`, so ``gma/events`` is required
in the dependency list.


Currying
++++++++

This example can be simplified by using currying. Currying a function with
arguments returns a function that calls the original function with the arguments
provided. For example, the following function (``f1`` and ``f2``) are equivalent;
to create ``f2``, the move function is `curried` with the first of it's argument
(`direction`) to create a function with the keyboard event as the only argument:

.. code-block:: javascript

    f1 = function (keyEvent) {
        manager.character.move(gma.constants.LEFT, keyEvent);
    };
    f2 = manager.character.move.curry(gma.constants.LEFT);

Therefore the keybinding example can be simplified to:

.. code-block:: javascript

    gma.keyHandler.register(37, manager.character.move.curry(gma.constants.LEFT);
    gma.keyHandler.register(39, manager.character.move.curry(gma.constants.RIGHT);
    gma.keyHandler.register(32, manager.character.jump);


End result
----------

.. code-block:: javascript

    require([
        'gma/base',
        'gma/manager',
        'gma/entities/character',
        'gma/events'
    ],
        function(gma) {
            var manager = gma.manager({
                width : 600,
                height : 500
            });
            manager.character = gma.character({
                left     : 0,
                bottom   : 0,
                width    : 3,
                height   : 6,
                depth    : 3
            });

            var myLevel = {
                spawn : {
                    main : [15, 24]
                },
                entities : [
                    {top:0, left:0, width:30, height:3},
                    {top:0, left:36, width:30, height:3}
                ]
            };
            manager.storeLevels(myLevel);

            gma.keyHandler.register(37, manager.character.move.curry(gma.constants.LEFT));
            gma.keyHandler.register(39, manager.character.move.curry(gma.constants.RIGHT));
            gma.keyHandler.register(32, manager.character.jump);

            manager.init();
        }
    );

What's next?
------------

In the next section we will :doc:`create some enemies <enemies>`.
