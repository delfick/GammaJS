.. _levelSpecs:

Levels
======

A level specification is created to specify what is inside a game.
This is used to tell the game engine the position, appearance and behaviour of
any objects in each level.


Specifying Levels
-----------------

A level specification is a normal Javascript object with particular properties.
A level needs at minimum, a spawn location for the character and a camera.
Gamma will provide defaults if these properties are not specified.
This means that you can provide an empty object and Gamma will still be able
to start a working level.

.. note:: The advanced topic on :ref:`levelParsers` describes what is provided
    on the level by default, and how to customise this behaviour.

.. _spawnPoints:

Adding Spawn points
+++++++++++++++++++

A :term:`spawn point` is a location in 2D space with a label attached to it.

Spawn points are commonly used by Gamma to set the position of the character
when a level is loaded. To do this, a level must specify a spawn point withthe
label ``main``. If no such location is specified, then one is added to the level
at [0, 0].

Spawn points are specified as a :term:`hash` that associates a label to a
[x, y] co-ordinate.

.. code-block:: javascript

    var myLevel = {
        spawn : {
            main: [5,30],
            someOtherLocation : [20, 65]
        }
    }

.. note:: As shown in the :ref:`initialisingLevels` section, it is possible to
    change which spawn point is used to :term:`spawn` the character when the
    level is loaded


Customising the camera
++++++++++++++++++++++

To customise the camera, you may specify options under the ``camera`` label.
All of the options provided by the :glge:`GLGE Camera <Camera>` are available
(look for the the ``set*`` functions).

To make an orthographic camera, 50 units from the origin:

.. code-block:: javascript

    var myLevel = {
        camera : {
            locZ : 50,
            type : GLGE.C_ORTHO
        }
    }


.. _lights:

Adding Lights
+++++++++++++

You can add lights to your level by specifying them inside a :term:`hash` under
the label ``light``.

.. code-block:: javascript

    var myLevel = {
        light : {
            light1 : {},
            light2 : {},
            light3 : {}
        }
    }

You can find all the options you can set by finding all the ``set*`` functions
over :glge:`here <Light>`.

For example,

.. code-block:: javascript

    var myLevel = {

        light : {
            spotlight1 : {
                rotY : 1.54,
                locZ : -50,
                type : GLGE.L_POINT,

                color    : "#fff",
                rotOrder : GLGE.ROT_XZY,

                attenuationLinear    : 0.0,
                attenuationConstant  : 2.0,
                attenuationQuadratic : 0.00
            }
        },
    }


.. _attached:

Attaching Lights and Camera to the character
++++++++++++++++++++++++++++++++++++++++++++

When specifying your camera and lights, you may also specify an ``attached``
option, which will cause that camera/light to follow some other entity.
When you specify ``attached``, you provide an array that contains at least a
string specifying the entity to follow. You may then optionally specify
``x``, ``y`` and ``z`` offsets.

For example,

.. code-block:: javascript

    var myLevel = {
        camera : {
            locZ : -50,
            attached : ['character']
        },

        light : {
            spotlight : {
                attached : ['character', 0, 3]
            }
        }
    }

When you don't specify ``x`` or ``y`` offsets, they will default to zero.
If there is no ``z`` offset the z-position of the object will be set to
``locZ`` (which defaults to 0). So in the above example, the camera will follow
the movement of the character (but 50 units towards the viewer) and the light
will always be 3 units above where the character is.

.. note:: For now, Gamma only allows you to follow the character, but this may
    change in the future.


.. _levelSpec_entities:

Adding Entities
+++++++++++++++

Entities may be specified as a list of Gamma objects:

.. code-block:: javascript

    var myLevel = {
        entities : [
            gma.door({x:0, y:9, width:5, height:6}),
            gma.door({x:15, y:9, width:5, height:6}),
            gma.enemy({x:9, y:9, width:1, height:2}),
            gma.platform({left:-9, right:18, top:9, height:3})
        ]
    };

This example creates a platform with an enemy and two doors sitting on it.

.. note::

    Your character object should be attached to the manager, not the level.
    Therefore the following will break some functionality the manager provides:

    .. code-block:: javascript

        var myLevel = {
            entities : [
                gma.character({x:0, y:9, width:5, height:6}),
            ]
        };

Templates
+++++++++

By default, all entities will be rendered as a :term:`rectangular prism` using
:prop:`gma.gma.unitCube`. You can change the template used by setting the
template property on the entity. Gamma provides 3 different templates for
rendering as described in the :ref:`appearance section <appearance>`.
This example will render a gorilla collada file instead of the default unit cube:

.. code-block:: javascript

    var myGorilla = gma.colladaTemplate({
        collada : {
            document : 'gorilla.dae'
        }
    });

    var myLevel = {
        entities : [
            gma.enemy({x:0, y:9, width:5, height:6, template:myGorilla}),
        ]
    };

Gamma also provides another default template, ``redcube``. This will render a
red cube instead of a blue cube.

.. code-block:: javascript

    var myLevel = {
        entities : [
            {left:19, right:30, top:9, height:3, template : 'redcube'}
        ]
    };

Removing Repetition
-------------------

.. _levelSpec_types:

Types
+++++

Types can be used to remove repetition when defining similar objects. A ``type``
is a specification of attributes, which can be associated with an object through
it's ``type`` property. For example to create a type ``shinyDoor`` that creates
a :api:`gma.door` with a width, height and depth of 4:

.. code-block:: javascript

    var myLevel = {
        types : {
            shinyDoor: ['door', {
                width    : 4,
                depth    : 4,
                height   : 4,
            }]
        }
    };

To assign this type to two objects:

.. code-block:: javascript

    var myLevel = {
        entities : [
            {type: 'shinyDoor', x:0, y:9}
            {type: 'shinyDoor', x:15, y:9}
        ],

        //Types same as above
        types : {
            shinyDoor: ['door', {
                width    : 4,
                depth    : 4,
                height   : 4,
            }]
        }
    };

By default, specifications will have the ``default`` type, which creates a
:api:`gma.platform`, so a platform in our level could be specified as:

.. code-block:: javascript

    entities : [
        {left:-9, right:18, top:9, height:3}
    ];

You can also override attributes specified in the type. For example:

.. code-block:: javascript

    var myLevel = {
        types : {
            myEnemy : ['enemy', {width:1, height:4}]
        },

        entities : [
            {type:'myEnemy', x:9, y:9, height:2}
            //height is now 2
        ]
    };



.. _replicateWith:

Replicating objects
+++++++++++++++++++

Gamma provides the ability to replicate options on a list of objects through
a ``replicateWith`` property.

ReplicateWith will create an object for each set of attributes in the array
passed to it. This object will have these attributes as well as the attributes
of the object ``replicateWith`` was defined in.

For example:

.. code-block:: javascript

    var myLevel = {
        entities : [
            {width:5, height:5, replicateWith : [
                {left:0, top:5},
                {left:7, top:5},
                {left:12, top:5},
                {left:17, top:5},
                {left:25, top:5}
            ]}
        ]
    };

is equivalent to

.. code-block:: javascript

    var myLevel = {
        entities : [
            {width:5, height:5, left:0, top:5},
            {width:5, height:5, left:7, top:5},
            {width:5, height:5, left:12, top:5},
            {width:5, height:5, left:17, top:5},
            {width:5, height:5, left:25, top:5}
        ]
    };

You can also ``replicateWith`` recursively. For example you could do the
following:

.. code-block:: javascript

    var myObject = gma.utils.expandReplicateWith({
        entities : [
            {optionA : 5, optionB : 6, optionC : 7, replicateWith : [
                {optionD : 8, optionE : 10, replicateWith : [
                    {optionF : 8, optionA : 5},
                    {optionF : 10, optionG : 11}
                ]},
                {optionD : 9, replicateWith : [
                    {optionF : 8},
                    {optionF : 10}
                ]},
            ]}
        ]
    })

Which is equivalent to:

.. code-block:: javascript

    var myObject = gma.utils.expandReplicateWith({
        entities : [
            {optionA : 5, optionB : 6, optionC : 7, replicateWith : [
                {optionD : 8, optionE : 10, optionF : 8, optionA : 5},
                {optionD : 8, optionE : 10, optionF : 10, optionG : 11},
                {optionD : 9, optionF : 8},
                {optionD : 9, optionF : 10}
            ]}
        ]
    })

Which is equivalent to:

.. code-block:: javascript

    var myObject = gma.utils.expandReplicateWith({
        entities : [
            {optionB : 6, optionC : 7, optionD : 8, optionE : 10, optionF : 8, optionA : 5},
            {optionA : 5, optionB : 6, optionC : 7, optionD : 8, optionE : 10, optionF : 10, optionG : 11},
            {optionA : 5, optionB : 6, optionC : 7, optionD : 9, optionF : 8},
            {optionA : 5, optionB : 6, optionC : 7, optionD : 9, optionF : 10}
        ]
    })


Adding Levels
-------------

Once you've created a :api:`gma.manager`, adding levels is as simple as calling
:metho:`gma.manager.storeLevels` with one or more level specifications

.. code-block:: javascript

    // We either call storeLevels with one level specification
    manager.storeLevels(someSpecification);

    // Or we call storeLevels with an array of one or more specifications and it will store them all
    manager.storeLevels([levelSpecification1, levelSpecification2, levelSpecification3]);


.. note:: Storing a level does not load it. Loading levels is explaining in the :ref:`initialisingLevels` section below.


.. _initialisingLevels:

Initialising Levels
-------------------

Once you've stored one or more levels on the manager using
:metho:`gma.manager.storeLevels`, you can use :metho:`gma.manager.loadLevel`
to load one of them.

For example

.. code-block:: javascript

    var manager = gma.manager();
    manager.storeLevels({});
    manager.loadLevel()

By default, :metho:`gma.manager.loadLevel` will load the first level that has
been stored on the manager and will spawn the :prop:`gma.manager.character` at
the spawn point with label ``main``.

However, you can specify which level you wish to load, and at which spawn point.

.. code-block:: javascript

    // Create some level specifications
    var level1 = {};
    var level2 = {spawn : {other : [0, 9]}};
    var level3 = {};

    // Store the levels on manager
    manager.storeLevels([level1, level2, level3])

    // Load the second level
    // Note that the levels are zero indexed
    manager.loadLevel(1)

    // Or we could load the second level, and spawn the character at the spawn point labelled "other"
    manager.loadLevel(1, "other")

.. note:: The list of levels on the manager is zero indexed. This means the
    first level is at index 0, the second level is at index 1, etc.

Once you've loaded a level, :metho:`gma.manager.twitch` is started, and the
:term:`Game Loop` will cause a cycle of animating, removing "killed" entities,
and rendering.
