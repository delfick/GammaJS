Add some polish to your game
============================

Congratualations! You have reached the last part of the tutorial series!

Stop Falling Forever
--------------------

Currently if you fall off the platform you will fall forever. To stop the
character falling infinitely we can put a platform below which will kill the
character when fall onto it. Gamma provides the :api:`gma.deathPlatform` for
this purpose. Let's create one under the main platforms and paint it red:

.. code-block:: javascript

    // Create a deathplatform type
    types : {
        lava : ['deathPlatform', {template : 'redcube', depth:50}]
    }
    // Add this lava / death platform to the list of entities
    entities : [
        {type:'lava', top:-10, left:-50, width:1000, height:50},
    ]

Respawn the Character
---------------------
We will also bind a key to respawn the character (for when it dies).
Register the method :metho:`gma.manager.respawn` to be called when the letter
'r' (for reload/restart/respawn) is pressed:

.. code-block:: javascript

    gma.keyHandler.register(82, function(e) {
        manager.respawn("main");
    });

The last `Final result`
-----------------------

Now that you've finished, the game description (``game.js``) should look very
similar to this:

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
                    }],
                    lava : ['deathPlatform', {template : 'redcube', depth:50}]
                }

            });

            manager.hud.setup({
                bottom_right: {
                    fps : manager.getFPS
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
                    {type:'deathPlatform', top:-10, left:-50, width:1000, height:50, depth:50},
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
                    {template:'brickscube', top:0, left:0, width:30, height:3},
                    {type:'deathPlatform', top:-10, left:-50, width:1000, height:50, depth:50}
                ]
            };

            manager.storeLevels(myLevel);
            manager.storeLevels(otherLevel);

            gma.keyHandler.register(37, manager.character.move.curry(gma.constants.LEFT));
            gma.keyHandler.register(39, manager.character.move.curry(gma.constants.RIGHT));
            gma.keyHandler.register(32, manager.character.jump);
            gma.keyHandler.register(82, function(e) { manager.respawn("main"); })
            manager.init();
        }
    );


What Now?
---------

We recommend that you try to make a bigger and funner game whilst you read parts
of the :ref:`simpleTopics` section, and if you really want a customised game,

