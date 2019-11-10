Add a character
===============

To specify a character, we need to create an instance of :api:`gma.character`
and assign it to :prop:`manager.character <gma.manager.character>`.
We create a character with a position and dimensions:

.. code-block:: javascript

    manager.character = gma.character({
        left     : 0,
        bottom   : 0,
        width    : 3,
        height   : 6,
        depth    : 3
    });

We also need to add ``gma/entities/character`` to the dependency list of the
require function.


Setting the character spawn location
------------------------------------

A spawn point specifies the location where the character to appear. A spawn
point is associated with a label inside the level object. When a level is loaded,
it will place the character at the spawn point with the label ``main``.

Gamma expects the x and y coordinates of the bottom left corner of the
character's position. This example creates a spawn point labeled ``main`` at
x=15 and y=24:

.. code-block:: javascript

    var mylevel = {
        spawn : {
            main : [15, 24]
        }
    }

.. note:: When a level is processed, if it does not have a spawn point with the
    label ``main``, a spawn point is added with the location [0, 0]


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
            manager.init();
        }
    );


What's next?
------------

In the next section we will
:doc:`learn how to setup controls for the character <moving>`.
