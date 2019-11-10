
.. _platforms:

Platform
========

A platform is a entity in the game which the character stands on, runs on,
and jumps to and from.

A :api:`gma.platform` is defined by it's dimensions (height, width, depth) and
position (x, y). As with all :api:`rectangles <gma.shapes.rectangle>`,
this can be specified in :ref:`many different ways <definingShapes>`.
For example:

.. code-block:: javascript

    // 3 ways to specify the same platform.
    gma.platform({depth:20, left:10, width:20, bottom:10, height:5});
    gma.platform({depth:20, left:10, right:30, bottom:10, top:15});
    gma.platform({depth:20, x:20,    width:20, y:12.5,    height:5});


A non-solid platform
--------------------

Platforms can also be defined as solid or not via it's :prop:`gma.platform.solid`
property. If this is set to ``false``, then nothing can collide with the
platform,i.e. entities will go through it.

.. code-block:: javascript

    var cloud = gma.platform({
        x:0, y:0, width:1, height:1, depth: 20
        solid: false
    });


A deadly platform
-----------------

Platforms support the ``deathtouch`` tag. A platform with `deathtouch` will
"kill" any :api:`gma.character` that hits it. This tag is already specified when
you create a platform using :api:`gma.deathPlatform`.

.. code-block:: javascript

    var lava = gma.deathPlatform({
        x:10, y:-1, width:10, height:1, depth: 20
    });

    // Is equivalent to:
    var lava = gma.platform({
        x:10, y:-1, width:10, height:1, depth: 20
        tags : ["deathtouch"]
    });


Adding platforms to your game
-----------------------------

To add platforms to your game, they must be added to a
:ref:`level specification <levelSpecs>`, which is stored on the manager and
loaded. The example platforms above could be added to a level like this:

.. code-block:: javascript

    var aLevel = {
        types : {
            lava: ['deathplatform', {}]
        },
        entities : [
            // Normal Platform. Note the default entity type is platform
            {left:10, bottom:10, width:20, height:5, depth:20},

            // Non-solid platform
            {solid:false, x:0, y:0,  width:1, height:1, depth: 20},

            // Death Platform
            {type:"lava", x:0, y:-1, width:10, height:1, depth:20}
        ]
    };

    // Then add level to manager
    manager.storeLevels(aLevel);


See :ref:`levelSpec_entities` and :ref:`levelSpec_types`
(in the :ref:`levels  <levelSpecs>` topic) for an explanation of how the above
code works. (Particularly, to explain why we don't need to explicitly use
``gma.deathPlatform`` and ``gma.platform``.)
