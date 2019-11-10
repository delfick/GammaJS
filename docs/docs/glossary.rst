.. _glossary:

Glossary
========

.. glossary::

    Closure
        A closure is a first-class function which has access to variables
        declared in its surrounding scope. A closure is defined within the scope
        of its free variables, and the extent of those variables is at least as
        long as the lifetime of the closure itself. The explicit use of closures
        is associated with functional programming and with languages such as ML
        and Lisp. Closures are used to implement continuation passing style,
        and in this manner, hide state. Constructs such as objects and control
        structures can thus be implemented with closures.

    Curry
        Currying a function with arguments returns a function that calls the
        original function with the arguments provided. For example, the following
        function (``f1`` and ``f2``) are equivalent; to create ``f2``, the
        ``sayThing`` function is `curried` with the first of it's arguments
        (``verb``) to create a function with the second argument (``noun``) as
        the only argument:

        .. code-block:: javascript

            sayThing = function(verb, noun) {
                alert( "Why don't you " + verb + " the " + noun + "?")
            }

            f1 = function (noun) {
                sayThing("jump", noun);
            };
            f2 = sayThing.curry("jump");

    Dictionary
        Another word for :term:`Hash`. This term is used to highlight the
        key-value aspect of javascript objects.

    Game loop
        The game loop allows the game to run smoothly regardless of a user's
        input or lack thereof. A game loop will typically do the following:

        - check for user input
        - run AI
        - move enemies
        - resolve collisions
        - draw graphics
        - play sounds

    Hash
        A hash is simply a Javascript object, with a set of associated keys and
        values. For example:

        .. code-block:: javascript

            var thing = {
                key : "Value",
                another : [1, 2, 3, 4]
            };

        In other programming languages, a hash may be referred to as a
        struct(ure), or a dictionary.

    HUD
        A heads-up display (HUD) is any transparent display that presents data
        without requiring users to look away from their usual viewpoints.
        In Gamma, the HUD is an overlay used to display information to the game
        player (generally their score and lives).

    Minified
        Minified source code is code that has been stripped of all unnecessary
        characters from source code, resulting in code that is compressed and
        often obfuscated. Sometimes the minification process will combines
        multiple files.

    Rectangular prism
        A rectangular prism (or more accurately rectangular cuboid) is a solid
        shape bounded by 6 rectangular faces. All corners are right angles and
        it has a uniform height, width and depth. See `Rectangular cuboid on
        wikipedia <http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid>`_

    Recursion
        See :term:`recursion`.

    Scene
        The 3D environment, containing lights and objects, that is rendered
        and displayed to the player.

    Spawn
        Spawning is the in-game placement of an entity, such as a player
        character or enemy.

    Spawn point
        A spawn point is the coordinates at which a character or enemy can
        appear (or :term:`spawn`).
