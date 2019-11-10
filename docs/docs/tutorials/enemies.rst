Adding some enemies
===================

Gamma provides :ref:`a few enemy entities <enemies>` for you that have their
own behaviour. To add an enemy object to the level, you must specify the enemy
object in the entity list.

For this tutorial, we will create a :api:`gma.platformEnemy` (that walks from
one end a platform to the other), a :api:`gma.patrolEnemy` (that walks between
two points); and a few :api:`gma.jumpingEnemy`
(that jump on the spot repeatedly):

.. code-block:: javascript

    entities : [
        gma.platformEnemy({bottom:0, left:45, width:3, height:6}),
        gma.patrolEnemy({bottom:0, left:6, width:3, height:6, limitLeft: 3, limitRight:12}),
        gma.jumpingEnemy ({bottom:0, left:7,  width:1, height:2}),
        gma.jumpingEnemy ({bottom:3, left:8,  width:1, height:2}),
        gma.jumpingEnemy ({bottom:6, left:9,  width:1, height:2})
    ]

The platform and jumping enemy require only dimensions and position
(like platforms), but the patrol enemy also requires ``limitLeft`` and
``limitRight`` be set.

Types
-----

When we specify many entities with common attributes, we can move the attributes
into a custom `type`. This `type` can be referenced when making the entities to
avoid unnecessary repetition. We specify `types` using
:metho:`gma.manager.addCustomDefinitions`. For example:

.. code-block:: javascript

    manager.addCustomDefinitions({
        types : {
            jumpingJack: ['jumpingEnemy', {
                width    : 1,
                height   : 2
            }]
        }
    });

When specifying a `type`, you provide an array where the first element is the
name of the class to instantiate (:api:`gma.jumpingEnemy`) and the second
element is an object containing options which will be applied to all new
instances.

We can now create jumping enemies by referencing the ``jumpingJack`` `type` as
shown below:

.. code-block:: javascript

    // Now we can reference jumping jack
    entities : [
        gma.platformEnemy({bottom:0, left:45, width:3, height:6}),
        gma.patrolEnemy({bottom:0, left:6, width:3, height:6, limitLeft: 3, limitRight:12}),
        {type:'jumpingJack', bottom:0, left:21},
        {type:'jumpingJack', bottom:3, left:24},
        {type:'jumpingJack', bottom:6, left:27}
    ]

.. note:: We no longer use the :api:`gma.jumpingEnemy` function explicitly nor
    do we specify the width/height of these enemies.

Templates
---------

By default all entities are rendered as a blue rectangular prism. This is
controlled by the ``template`` property of the entity.
The default template is ``cube`` which could (redundantly) be set as follows:

.. code-block:: javascript

    manager.addCustomDefinitions({
        types : {
            jumpingJack: ['jumpingEnemy', {
                width    : 1,
                height   : 2
                template : 'cube'
            }
        }
    });

If you would like to customise the appearance of an entity you must first create
a `template`. Here, we will use the :api:`gma.meshTemplate` template helper to
create  a green rectangular prism template:

.. code-block:: javascript

    manager.addCustomDefinitions({,
        templates : {
            greencube : ['meshTemplate', {
                mesh : gma.unitCubeInfo.mesh,
                material : {color : "#090"}   // Very Green
            }
        }
    });

We can then apply this template to the ``jumpingJack`` type:

.. code-block:: javascript

    manager.addCustomDefinitions({
        types : {
            jumpingJack: ['jumpingEnemy', {
                width    : 1,
                height   : 2
                template : 'greencube'
            }
        }
    });

.. note::

    By default, ``cube`` and ``redcube`` templates already exist, which simply
    create a blue and red cube respectively. The :ref:`appearance` section
    outlines types of template objects that are available and how to use them.

    Also, by default, entities will have the ``default`` type, which simply
    creates a :api:`gma.platform` and uses the ``cube`` template.


End result
----------

.. code-block:: javascript

    require([
        'gma/base',
        'gma/manager',
        'gma/entities/character',
        'gma/events',
        'gma/entities/enemy'
    ], function(gma) {
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
                entities : [
                    {top:0, left:0, width:30, height:3},
                    {top:0, left:39, width:30, height:3},
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

In the next section we will :doc:`learn how to change the camera <camera>`.
