.. _collisionFunctions:

Defining collision behaviour
============================

Each entity in Gamma defines what happens when a collision with another entity
occurs via their :metho:`gma.shapes.rectangle.collided` method. When Gamma
:api:`detects that a collision has occurred <gma.collisions>`,
this function is invoked on the entities that have collided.

An understanding of this function is helpful if you wish to extend the
functionality of the character or enemies, or create new entities.

The *collided* method
*********************

For the following explanation, ``self`` refers to the entity defining the
behaviour, and ``focus`` refers to the entity that is being collided with.

The :metho:`gma.shapes.rectangle.collided` method accepts four arguments:

* ``where`` -- The side of ``self`` that was collided with as a :api:`gma.constant`
* ``focus`` -- The entity that was collided with
* ``focusSide`` -- The side of the ``focus`` that was collided with
* ``focusVector`` -- The movement vector [x, y] that the ``focus`` was trying
  to move by before it collided

To make configuring and customising behaviour flexible, we have implemented this
function so that it looks at the :ref:`tags <tags>` on the entity.
If a particular tag exists, then an internal method (with the same method
signature) is called to carry out the functionality.

In this example the function to pick up a collectable (eg. coin) is called if
the focus has a collectable tag:

.. code-block:: javascript

    var oldCollided = self.collided;
    self.collided = function(where, focus, focusSide, focusVector) {
        oldCollided.apply(this, arguments);
        if (focus.tags.collectable) {
            self.collided__pickupCollectable.apply(this, arguments);
        }
    };

In this extract from :api:`gma.enemy`, the focus (character) is killed if the
enemy is alive and has the ``deathtouch`` tag:

.. code-block:: javascript

    var oldCollided = self.collided;
    self.collided = function() {
        oldCollided.apply(this, arguments);
        ...

        if (self.alive && self.tags.deathtouch) {
            self.collided__deathtouch.apply(this, arguments);
        }
    };

    // Defined elsewhere
    self.collided__deathtouch || function(w, focus, fs, fv) {
        if (focus.tags.character) {
            focus.kill();
        }
    };

As a convention, these internal methods are named by prepending the tag name
with "collided\_\_". See :metho:`gma.enemy.collided__deathtouch`,
:metho:`gma.enemy.collided__weakhead`,
:metho:`gma.enemy.collided__rebound` and
:metho:`gma.character.collided__pickupCollectable`


Writing custom collision behaviour
**********************************

Let's say we want to make a `cryer` that yells in pain every time something hits
it.

To create a `cryer` we can create a rectangle and define a custom ``collided``
function on that rectangle. We create a reference of the old ``collided``
function before we define the new one. Then, inside the new ``collided``
function we invoke the old function:

.. code-block:: javascript

    myRectangle = gma.shapes.rectangle({x:0, y:0, width:1, height:1});

    oldCollided = myRectangle.collided;
    myRectangle.collided = function() {
        oldCollided.apply(this, arguments);
        manager.hud.message("OOOOWWWW", 20)
    }


Alternatively, we can create a function that can be used to add this
functionality to any entity.

.. code-block:: javascript

    cryerFunctionality = function(entity) {
        var self = entity || gma.shapes.rectangle({x:0, y:0, width:1, height:1});

        var oldCollided = self.collided;
        self.collided = function() {
            oldCollided && oldCollided.apply(this, arguments);
            manager.hud.message("OOOOWWWW", 20)
        }

        return self;
    }

If we follow the convention that this logic should be defined in an internal
function, would would write the function as:

.. code-block:: javascript

    cryerFunctionality = function(entity) {
        var self = entity || gma.shapes.rectangle({x:0, y:0, width:1, height:1});

        var oldCollided = self.collided;
        self.collided = function() {
            oldCollided && oldCollided.apply(this, arguments);
            self.collided__announce.apply(this, arguments);
        }

        self.collided__announce = function() {
            manager.hud.message("OOOOWWWW", 20)
        }

        return self;
    }

We could take this further and use the functions arguments to change the message:

.. code-block:: javascript

    cryerFunctionality = function(entity) {
        var self = entity || gma.shapes.rectangle({x:0, y:0, width:1, height:1});

        self.sides = {}
        self.sides[gma.constants.TOP]    = 'top'
        self.sides[gma.constants.LEFT]   = 'left'
        self.sides[gma.constants.RIGHT]  = 'right'
        self.sides[gma.constants.BOTTOM] = 'bottom'

        oldCollided = self.collided;
        self.collided = function() {
            oldCollided.apply(this, arguments);
            self.collided__announce.apply(this, arguments);
        }

        self.collided__announce = function(where, focus, focusSide) {
            manager.hud.message("OWWWWWW, damnit!, something hit my " + sides[where] + " with their " + sides[focusSide], 20);
        }

        return self;
    };

We could also change the message based on the entity's tags:

.. code-block:: javascript

    cryerFunctionality = function(entity) {
        var self = entity || gma.shapes.rectangle({x:0, y:0, width:1, height:1});

        self.sides = {}
        self.sides[gma.constants.TOP]    = 'top'
        self.sides[gma.constants.LEFT]   = 'left'
        self.sides[gma.constants.RIGHT]  = 'right'
        self.sides[gma.constants.BOTTOM] = 'bottom'

        oldCollided = self.collided;
        self.collided = function() {
            oldCollided.apply(this, arguments);
            if (self.tags.angry) {
                self.collided__anger.apply(this, arguements);
            }
            else {
                self.collided__announce.apply(this, arguments);
            }
        }

        self.collided__announce = function(where, environ, environSide) {
            manager.hud.message("OWWWWWW, damnit!, something hit my " + sides[where] + " with their " + sides[environSide], 20);
        }

        self.collided__anger = function(where, environ, environSide) {
            manager.hud.message("GO AWAY, ANNOYING THING", 20);
        }

        return self;
    };

We can then use it as follows:

.. code-block:: javascript

    captainObvious = gma.jumpingEnemy({x:0, y:0, width:2, height:5});
    cryerFunctionality(captainObvious);

    anAngryEnemy = gma.enemy({x:0, y:0, width:2, height:4, tags=['angry']});
    cryerFunctionality(anAngryEnemy);
