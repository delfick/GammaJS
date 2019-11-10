Add some platforms
==================

Lets create a very basic level containing a few platform. To add some platforms
to our game, they must be added to a level.

A platform it a type of entity. Therefore the platforms are specified in the
entities array inside the level. For example:

.. code-block:: javascript

    var myLevel = {
        entities : [
            {type: 'platform', top:0, left:0, width:30, height:3},
            {type: 'platform', top:0, left:36, width:30, height:3}
        ]
    };

As ``platform`` is the default entity, we could specify this as:

.. code-block:: javascript

    var myLevel = {
        entities : [
            {top:0, left:0, width:30, height:3},
            {top:0, left:36, width:30, height:3}
        ]
    };

Finally, we need to add the level to the manager using
:metho:`gma.manager.storeLevels`:

.. code-block:: javascript

    manager.storeLevels(myLevel);


End Result
----------

.. code-block:: javascript

    require(['gma/base', 'gma/manager'],

        function(gma) {
            var manager = gma.manager({
                width : 600,
                height : 500
            });
            var myLevel = {
                entities : [
                    {top:0, left:0, width:30, height:3},
                    {top:0, left:36, width:30, height:3}
                ]
            };
            manager.storeLevels(myLevel);
            manager.init();
        }
    );

.. Note:: To learn more about the various ways to specify a platform see
    :ref:`the platforms topic <platforms>`


What's next?
------------

In the next section we will :doc:`add a character to our game <character>`.
