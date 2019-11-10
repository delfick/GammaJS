.. _enemies:

Enemy
=====

A range of enemy objects are provided by :api:`gma.enemy`. An enemy object is
very similar to the :ref:`character` object, except that it is not controlled
by the player. Instead it follows a set of behaviour definitions to determine
it's movement.

Enemy Movement and Collision Behaviour
--------------------------------------

Gamma provides several behaviours which can be assigned to an enemy, by
specifying particular :ref:`tags <tags>` when you create the enemy.
These tags and the associated behaviour are described below:


Patrolling
++++++++++

The `patrolling` tag makes the enemy move back and forward between 2 specified
x coordinates.

It requires that the enemy has ``limitLeft`` and ``limitRight`` properties set
on it, which hold a number representing the left and right horizontal limit of
the enemy's `patrolling area` respectively.

.. note:: This is provided via :metho:`gma.enemy.behaviour__patrolling`,
    through :metho:`gma.enemy.determineState`.


Platformer
++++++++++

The `platformer` tag makes the enemy move back and forward between the edges of
the platform which it is currently standing on. The enemy will automatically
detect edges of the platform so no extra information is required when
declaring it.

.. note:: This is provided via :metho:`gma.enemy.behaviour__platformer`,
    through :metho:`gma.enemy.determineState`.


Jumping
+++++++

The `jumping` tag makes the enemy jump repeatedly on the spot. It is possible
to customize how high the enemy jumps by changing the value of it's
:prop:`gma.enemy.jumpVelocity` property.

.. note:: This is provided via :metho:`gma.enemy.behaviour__jumping`, through
    :metho:`gma.enemy.determineState`.


Deathtouch
++++++++++

Enemies with the `deathtouch` tag will kill a character if it collides with one.

.. note:: This is provided via :metho:`gma.enemy.collided__deathtouch`.
    See this :ref:`explanation of collision functions <collisionFunctions>`.

Rebound
+++++++

Enemies that have the `rebound` tag will turn around and walk in the opposite
direction if they collide with another entity.

.. note:: This is provided via :metho:`gma.enemy.collided__rebound`. See this
    :ref:`explanation of collision functions <collisionFunctions>`.

Weakhead
++++++++

The `weakhead` tag makes the top of the enemy vulnerable to :api:`gma.character`
objects. As in, if a character jumps on top of an enemy that has this tag,
that enemy will be "killed".

This functionality has precedence over `deathtouch`, such that you can kill an
enemy with `deathtouch` without dying.

.. note:: This is provided via :metho:`gma.enemy.collided__weakhead`.
    See this :ref:`explanation of collision functions <collisionFunctions>`.


Predefined Enemies
------------------

Gamma also provides some convenience objects for you that already have particular
tags defined on them.

All of them have ``weakhead`` and ``deathtouch`` tags by default.

:api:`gma.patrolEnemy`
++++++++++++++++++++++

This object also has ``rebound`` and ``patrolling`` tags

.. code-block:: javascript

    var turtle = gma.patrolEnemy({
        x:0, y:0, width:1, height:1,
        limitLeft: 20,
        limitRight: 40
    });

    // Is equivalent to

    var turtle = gma.enemy({
        x:0, y:0, width:1, height:1,
        tags: ['weakhead', 'deathtouch', 'rebound', 'patrolling'],
        limitLeft: 20,
        limitRight: 40
    });

:api:`gma.jumpingEnemy`
+++++++++++++++++++++++

This object also has a ``jumping`` tag.

.. code-block:: javascript

    platform_turtle = gma.jumpingEnemy({
        x:0, y:0, width:1, height:1,
    });

    // Is equivalent to

    var turtle = gma.enemy({
        x:0, y:0, width:1, height:1,
        tags: ['weakhead', 'deathtouch', 'jumping']
    });

:api:`gma.platformEnemy`
++++++++++++++++++++++++

This object also has ``rebound`` and ``platformer`` tags

.. code-block:: javascript

    platformer = gma.platformEnemy({
        x:0, y:0, width:1, height:1,
    });

    // Is equivalent to

    var turtle = gma.enemy({
        x:0, y:0, width:1, height:1,
        tags: ['weakhead', 'deathtouch', 'rebound', 'platformer']
    });


.. _adventure:

Create Your Own Enemy Definition
--------------------------------

As these behaviours and enemy interactions are based on tags, you can define
your own combination of enemy behaviours. This example creates a patrolling
:api:`gma.enemy` that doesn't die if you jump on it (no `weakhead` tag) and
won't turn around until it reaches the end of it's patrol (no `rebound` tag)

.. code-block:: javascript

    var onyx_one = gma.enemy({
        tags: ["deathtouch", "patrolling"],
        x:30, y:0, width:1, height:1,
        limitLeft: 20,
        limitRight: 40
    });

To make this into a reusable definition, create a function that calls gma.enemy
and modifies the result:

.. code-block:: javascript

    gma.onyx = function(spec) {
        var self = gma.enemy(spec);
        self.tags.deathtouch = true;
        self.tags.patrolling = true;
        return self;
    };

    // Example of using the new definition
    var onyx_two = gma.onyx({
        x:50, y:0, width:1, height:1,
        limitLeft: 40,
        limitRight: 60
    });
