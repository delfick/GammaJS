Creating multiple Levels
========================

Making multiple levels requires you to define multiple level specifications.
For Example:

.. code-block:: javascript

    var myLevel = {
        //specification
    };
    var anotherLevel = {
        //specification
    };

You will then need to call :metho:`gma.manager.storeLevels` multiple times with
each level:

.. code-block:: javascript

    manager.storeLevels(myLevel);
    manager.storeLevels(anotherLevel);

Or once with an array of levels:

.. code-block:: javascript

    manager.storeLevels([myLevel, anotherLevel]);


When ``manager.init()`` is called **the first level stored will be loaded**.
Now we just need a way of going from one level to another. This is achieved with
a door.

Create a door
-------------

Gamma provides a :api:`gma.door` entity that you can place in a level.
When touched by the character, it will ask the manager to load another level for
you.

To add a door to your level specification you will need to add
``gma/entities/door`` to the dependency list.
Then specify a :api:`gma.door <gma.door>` with dimensions and a level to load
when the character collides with it. The door should be added to the list of
entities in ``myLevel``:

.. code-block:: javascript

    entities : [
        gma.door({
            bottom:0, left:5, width:3, height:3,
            level:1
        })
    ]

.. note::
    The number accepted by the ``level`` attribute determines which level to
    load. Note that because arrays in JavaScript are zero-indexed the first
    level is at index 0, the second at index 1, etc. Levels are indexed in the
    order they are added:

    .. code-block:: javascript

        manager.storeLevels([myLevel, anotherLevel]);
        manager.storeLevels(hardLevel);
        // level:0 loads myLevel, stored at index 0
        // level:1 loads anotherLevel, stored at index 1
        // level:2 loads hardLevel, stored at index 2

Create another level
--------------------

Now create a second level with a platform supporting a door that leads back to
the first level:

.. code-block:: javascript

        var otherLevel = {
            spawn : {
                main : [0, 0]
            },
            camera : {
                attached : ['character', 0, 6, 60]
            },
            light : {
                myLight : {
                     type : GLGE.L_POINT,
                     rotY : 1.54,
                     color    : "#fff",
                     attached : ['character', 0,5,20]
                }
             },
            entities : [
                gma.door({bottom:0, left:25, width:0.5, height:9, level:0}),
                {template:'brickscube', top:0, left:0, width:30, height:3}
            ]
        };

Store ``otherLevel`` in the manager (after storing ``myLevel``):

.. code-block:: javascript

        manager.storeLevels(myLevel);    // Level:0
        manager.storeLevels(otherLevel); // Level:1


End Result
----------

The end result is 2 levels which can be travelled between via doors:

.. code-block:: javascript

    require([
        'gma/base',
        'gma/manager',
        'gma/entities/character',
        'gma/events',
        'gma/entities/enemy',
        'gma/entities/door'
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
                depth    : 3,
                template : 'gorilla'
            });
            manager.addCustomDefinitions({
                templates : {
                    greencube : ['meshTemplate', {
                        mesh : gma.unitCubeInfo.mesh,
                        material : {color : "#090"}
                    }],
                    gorilla : ['colladaTemplate',
                    {
                        collada : {
                            document : 'gorilla.dae'
                        },
                        yRot : 1.57,
                        yOffset : -0.5,
                        yScale:0.7
                    }],
                    brickscube : ['meshTemplate', {
                        mesh : gma.unitCubeInfo.mesh,
                        texture : {
                            src:'bricks.jpg',
                            repeatX:0.5,
                            repeatY:0.5
                        }
                    }]
                },

                types : {
                    jumpingJack: ['jumpingEnemy', {
                        width    : 1,
                        height   : 2,
                        template : 'greencube'
                    }]
                }
            });

            var myLevel = {
                spawn : {
                    main : [15, 24]
                },
                camera : {
                    attached : ['character', 0, 6, 60]
                },
                light : {
                    myLight : {
                         type : GLGE.L_POINT,
                         rotY : 1.54,
                         color    : "#fff",
                         attached : ['character', 0,5,20]
                    }
                 },
                entities : [
                    gma.door({bottom:0, left:55, width:0.5, height:9, level:1}),
                    {template:'brickscube', top:0, left:0, width:30, height:3},
                    {template:'brickscube', top:0, left:39, width:30, height:3},
                    gma.platformEnemy({bottom:0, left:45, width:3, height:6}),
                    gma.patrolEnemy({bottom:0, left:6, width:3, height:6, limitLeft: 3, limitRight:12}),
                    {type:'jumpingJack', bottom:0, left:21},
                    {type:'jumpingJack', bottom:3, left:24},
                    {type:'jumpingJack', bottom:6, left:27}
                ]
            };

            var otherLevel = {
                spawn : {
                    main : [0, 0]
                },
                camera : {
                    attached : ['character', 0, 6, 60]
                },
                light : {
                    myLight : {
                         type : GLGE.L_POINT,
                         rotY : 1.54,
                         color    : "#fff",
                         attached : ['character', 0,5,20]
                    }
                 },
                entities : [
                    gma.door({bottom:0, left:25, width:0.5, height:9, level:0}),
                    {template:'brickscube', top:0, left:0, width:30, height:3}
                ]
            };

            manager.storeLevels(myLevel);
            manager.storeLevels(otherLevel)

            gma.keyHandler.register(37, manager.character.move.curry(gma.constants.LEFT));
            gma.keyHandler.register(39, manager.character.move.curry(gma.constants.RIGHT));
            gma.keyHandler.register(32, manager.character.jump);
            manager.init();
        }
    );


What's next?
------------

In the next section we will
:doc:`learn how to give out game a heads up display <hud>`.
