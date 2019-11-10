Using Collada
=============

`Collada <https://collada.org>`_ is open standard xml schema to define a model.
Most 3D modelling applications support exporting models in this format
(a .dae file).

For this tutorial we will use
`a gorilla model <https://github.com/Royce/GammaJS/raw/master/media/collada/gorilla/gorilla.dae>`_
to represent the character. Download the
`gorilla model <https://github.com/Royce/GammaJS/raw/master/media/collada/gorilla/gorilla.dae>`_
and the
`gorilla's texture file <https://github.com/Royce/GammaJS/raw/master/media/collada/gorilla/skin.jpg>`_
and put them in the same directory.

Create a collada template
-------------------------

To assign our model to an entity you must (again) create a template. We will use
the :api:`gma.colladaTemplate` object to create a 3D object from a collada file.
We specify the location of the collada file inside a template named ``gorilla``:

.. code-block:: javascript

    manager.addCustomDefinitions({
        templates : {
            gorilla : ['colladaTemplate',
                {
                    collada : {
                        document : 'gorilla.dae'
                    }
                }
            ]
        }
    })

Unfortunately the gorilla is facing the wrong direction and not centered
correctly. To fix this we will rotate the model by 180 degrees (1.57 radians),
move it 0.5 units down and scale it by 0.7 vertically:

.. code-block:: javascript

    manager.addCustomDefinitions({
        templates : {
            gorilla : ['colladaTemplate',
                {
                    collada : {
                        document : 'gorilla.dae'
                    },
                    yRot : 1.57,
                    yOffset : -0.5,
                    yScale : 0.7
                }
            ]
        }
    })

.. note::
    Loading the Collada file requires that your game's JavaScript file and the
    collada model are both fetched via http and from the same server.
    Accessing your game via the local filesystem (without a server) will not
    work.

    If the url in the browser starts with "file:///" then you're accessing your
    game straight from the local filesystem. You will need to serve you files
    from a web server like `Apache <http://httpd.apache.org/>`_,
    `Lighttpd <http://www.lighttpd.net/>`_ or `IIS <http://www.iis.net/>`_

Assign the template to the character
------------------------------------

Assign this new template to the character, and you're done:

.. code-block:: javascript

    manager.character = gma.character({
        left     : 0,
        bottom   : 0,
        width    : 3,
        height   : 6,
        depth    : 3,
        template : 'gorilla'
    });

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
                depth    : 3,
                template : 'gorilla'
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
                    }],
                    gorilla : ['colladaTemplate'
                        {
                            collada : {
                                document : 'gorilla.dae'
                            },
                            yRot : 1.57,
                            yOffset : -0.5,
                            yScale : 0.7
                        }
                    ]
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

In the next section we will :doc:`learn how make multiple levels <extraLevels>`.
