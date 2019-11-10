Create a Heads Up Display (HUD)
===============================

The :term:`HUD` is used to display information, such as lives and score, to the
player.

Specifying a HUD
----------------

To specify a hud in your game, you must call :metho:`gma.hud.setup` on
:prop:`manager.hud <gma.manager.hud>` with a specification of what information
you want displayed and where:

.. code-block:: javascript

    manager.hud.setup(specification);

The specification is an object with keys matching the positions of where we wish
to display information in the HUD. Each position is passed information about
what data you wish to be displayed within this area as well as what heading you
wish it to be displayed under. This example will display the score number under
the label 'Score' in the top left corner:


.. code-block:: javascript

    manager.hud.setup({
        top_left: {
            "Score": function() {return character.score;}
        }
    });

For this tutorial we will make a HUD which displays the frames per second (FPS)
of your game in the bottom right corner:

.. code-block:: javascript

    manager.hud.setup({
        bottom_right: {
            fps : manager.getFPS
        }
    });

Styling and position the HUD
----------------------------

The appearance and position of each section is controlled by CSS, not the
``hud`` object. The following style sheet can be used to style the information
display by the HUD:

.. code-block:: css

    /* Setup the bars */

    #top_hud, #bottom_hud {
        height:2em;
        position:absolute;
        left:0em;
        width:100%;
        background-color: black;
        color: white;
        background-color: rgba(0, 0, 0, 0.7);
    }

    #top_hud {
        top:0em;
    }
    #bottom_hud {
        bottom:0em;
    }

    /* Setup left and right part of each bar */

    #bottom_hud dl, #top_hud dl {
        margin: 0.3em;
    }

    #bottom_hud dl.left, #top_hud dl.left {
        float: left;
    }
    #bottom_hud dl.right, #top_hud dl.right {
        float: right;
    }

    /* Setup labels for each item */

    #bottom_hud dt, #top_hud dt,
    #bottom_hud dd, #top_hud dd {
        display: inline-block;
        line-height: 1.4em;
        margin: 0;
    }

    #bottom_hud dt, #top_hud dt {
        padding-right: 0.5em;
    }

    #bottom_hud dd, #top_hud dd {
        text-align: right;
    }
    dl.left dd {
        padding-right: 1em;
    }
    dl.right dt {
        padding-left: 1em;
    }

Copy the CSS into ``game.css`` in the same directory as your ``game.js`` file.
Then uncomment this line in the HTML file:

.. code-block:: html

    <!--
        Include any style sheets here
        <link rel="stylesheet" type="text/css" href="gamma.css" media="all"/>
    -->


.. Note:: To learn more about the various ways to specify a HUD see
    :doc:`the hud topic </docs/topics/hud>`

End Result
----------

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
            manager.hud.setup({
                bottom_right: {
                    fps : manager.getFPS
                }
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
            manager.storeLevels(otherLevel);

            gma.keyHandler.register(37, manager.character.move.curry(gma.constants.LEFT));
            gma.keyHandler.register(39, manager.character.move.curry(gma.constants.RIGHT));
            gma.keyHandler.register(32, manager.character.jump);
            manager.init();
        }
    );


What's next?
------------

In the next section we will :doc:`add some 'polish' to your game <polish>`.
