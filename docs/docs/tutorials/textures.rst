Adding textures
===============

To apply a texture to an entity you must first define a template. As when
creating the ``greencube`` template (for the enemies), we will use the
:api:`gma.meshTemplate` object to create a rectangular prism.
We will assign a brick texture to the material of a new template and assign
this template to our platforms:

.. code-block:: javascript

    manager.addCustomDefinitions({
        templates : {
            brickscube : ['meshTemplate', {
                mesh : gma.unitCubeInfo.mesh,
                material : {texture : 'bricks.jpg'}
            }]
        }
    });

.. note:: For this to work, you will need a file called ``bricks.jpg`` in the
    same folder as your HTML. You can either make your own, or just
    `download ours <https://github.com/Royce/GammaJS/raw/master/media/textures/bricks.jpg>`_.

The texture will loop once for every unit of height and width. For our brick
texture, however, we want the bricks to be larger.
This is achieved by decreasing the amount the texture is looped for every unit
using the ``repeatX`` and ``repeatY`` attributes.

.. code-block:: javascript

    manager.addCustomDefinitions({
        templates : {
            brickscube : ['meshTemplate', {
                mesh : gma.unitCubeInfo.mesh,
                material : {
                    texture : 'bricks.jpg',
                    //This will make the bricks double the size
                    repeatX : 0.5,
                    repeatY : 0.5
                }
            }]
        }
    });

You can and should append this new template after the original ``greencube``
template. This is shown below in the end result.

Finally, we need to assign this template to the platforms:

.. code-block:: javascript

    var myLevel = {
        ...,
        entities : [
            {template:'brickscube', top:0, left:0, width:30, height:3},
            {template:'brickscube', top:0, left:39, width:30, height:3},
            ...
            // Enemy specifications removed for clarity
        ]
    };


End result
----------

.. code-block:: javascript

    require([
        'gma/base',
        'gma/manager',
        'gma/entities/character',
        'gma/events',
        'gma/entities/enemy'
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
            manager.addCustomDefinitions({
                templates : {
                    greencube : ['meshTemplate', {
                        mesh : gma.unitCubeInfo.mesh,
                        material : {color : "#090"}
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
                    {template:'brickscube', top:0, left:0, width:30, height:3},
                    {template:'brickscube', top:0, left:39, width:30, height:3},
                    gma.platformEnemy({bottom:0, left:45, width:3, height:6}),
                    gma.patrolEnemy({bottom:0, left:6, width:3, height:6, limitLeft: 3, limitRight:12}),
                    {type:'jumpingJack', bottom:0, left:21},
                    {type:'jumpingJack', bottom:3, left:24},
                    {type:'jumpingJack', bottom:6, left:27}
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

In the next section we will :doc:`learn how to load a collada model <collada>`.
