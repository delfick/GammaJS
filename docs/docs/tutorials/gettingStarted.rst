Getting Started
===============

See :ref:`the install guide <install>` to find out how to setup the game.
Once you've done this your ``game.js`` will contain the following.

.. code-block:: javascript

    require(['gma/base', 'gma/manager'],

        function(gma) {
            // The game specification is contained within this function.
            var manager = gma.manager();
            manager.storeLevels({});
            manager.init();
        }
    );

The require function
--------------------

The first thing  you will notice about ``game.js`` is that we "import" the
required parts of the Gamma library, by using the require method.
The require method takes in a list of dependencies to import from the Gamma
library (``gma/base`` and ``gma/manager``) and a function that is executed
when all these dependencies are resolved.

.. code-block:: javascript

    /*global require */
    require(['gma/base', 'gma/manager'],

        function(gma) {
            // The game specification is contained within this function.
            ...
        }
    );

The sole argument to this function is the :api:`gma` package.

Creating a canvas
-----------------

The second thing you will notice is ``var manager = gma.manager();``. This will
, by default, create a canvas inside a div with id of "gamma".
(Set the manager's :prop:`gma.manager.containerID` property when creating the
manager, to change this. See also: :prop:`gma.manager.container` and
:prop:`gma.manager.canvas`.)

You can control the height and width of the canvas by setting the manager's
:prop:`gma.manager.width` and :prop:`gma.manager.height` properties when you
create the manager. This example creates a canvas with width and height of 600
and 500 respectively:

.. code-block:: javascript

    /*global require */
    require(['gma/base', 'gma/manager'],

        function(gma) {
            var manager = gma.manager({
                width : 600,
                height : 500
            });
        }
    );


Starting the game loop
----------------------

To make our game actually run, we must initiate the :term:`Game loop`.
To do this we need to store a level on the manager and call it's init method.
In this case we are storing an empty level:

.. code-block:: javascript

    manager.storeLevels({});
    manager.init();


What's next?
------------

In the next section we will
:doc:`create a very basic level containing a few platforms <platforms>`.
