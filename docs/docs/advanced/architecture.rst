Architecture
============

If you are planning to extend or modify the Gamma framework -- or are, perhaps,
simply curious -- it is desirable to understand the various patterns that were
used whilst constructing the framework.

Reading this section, you will learn:

    - how to use `RequireJS <http://requirejs.org/>`_;
    - how each module is put in the gma namespace;
    - how we've constructed the building blocks in Gamma to allow inheritance;
    - how we've allowed private variables through closures; and
    - the limitations we imposed on the game engine for simplicity.


.. _requireJSNS:

Namespace and RequireJS
-----------------------

Eveything in Gamma exists under the ``gma`` namespace, which has been achieved
using `RequireJS <http://requirejs.org/>`_.

Whether defining a new module with ``require.def`` or simply loading
dependencies with  ``require``, you need to supply a list of dependencies that
will be loaded before executing the supplied callback. RequireJS will then pass
in all these dependencies into callback function when it loads.
When defining a module, this callback function is expected to return the module
and is called the `Module's function`.

.. code-block:: javascript

    require.def('newModule',
        [
            'dependency1',
            'dependency2'
        ],
        function(dependency1, dependency2) {
            // Module's function

            return the_module;
        }
    );

Gamma uses the convention that each module has ``gma/base`` as the first
dependency, then the gma namespace will be the first argument to the module's
function. Then, each module will append it's contents straight onto the gma
namespace. Therefore only the gma base object will return a module.

For example, :api:`gma.character` is added to the gma namespace with the
following code:

.. code-block:: javascript

    require.def('gma/entities/character',
        [ 'gma/base',              // Provides the gma namespace which
          'gma/entities/moveable', //  is passed into the function
          'gma/utils/collisions'   //  below.
        ],
        function(gma) {
            // Add gma.character
            gma.character = function(spec) {
                // character class goes here
            };
        }
    );


Factory Pattern
---------------

Gamma was designed so that `classes` behave like building blocks, allowing
objects to be created by applying many such "building blocks" to a JavaScript
object.

This was achieved using the factory pattern. In this pattern, an object is
created by a factory function that accepts an object and simply add more
properties/methods to it.

We have designed all our building blocks to "respect" properties/methods already
existing on any input object, by only setting such properties and methods if the
object doesn't already have such a property. The building blocks ensure that a
default set of properties/methods exist on objects, so that they may be
"complete".

For example,

.. code-block:: javascript

    var myClass = function(spec) {
        var self = spec || {};

        // add properties and methods to self
        self.y = self.y || 6

        self.someFunction = self.someFunction || function() {
            return 'hi there';
        };

        return self;
    };

    // Defaults to a new object if one isn't passed in
    var myNewObject = myClass();

    // Or we can apply the building block with some object
    var myOtherNewObject = myClass({x:5});
    myOtherNewObject.y; // <= 6

    // Or just by calling the function on an existing object
    var yetAnotherObject = {y:2};
    myClass(yetAnotherObject);
    yetAnotherObject.y; // <= 2

This allows the Gamma framework to imitate inheritance -- in the previous
example ``yetAnotherObject`` inherits from ``myClass`` -- but it is possible
to create an object that is built using a combination of unrelated blocks.

For example,

.. code-block:: javascript

    var myObject = {};
    // There are no building blocks as shape, animateable or
    //  armed, but for example's sake
    shape(myObject);
    animateable(myObject);
    armed(myObject);

.. note:: For all these examples to work, the factory must return the object
    it creates/edits at the bottom

The factory pattern also chosen because it allows our classes to have a
:term:`closure`, which allows us to imitate private variables.

.. code-block:: javascript

    var myClass = function(spec) {
        var self = spec || {};

        // Anything else that is var'd is private
        var secret = "Lalala";

        // Private variable is only exposed through an accessor
        self.someFunction = self.someFunction || function() {
            return 'My secret is ' + secret;
        };

        return self;
    };


Factories in collision detection
++++++++++++++++++++++++++++++++

We have also used factories for our collision detection for caching purposes,
as you can see on the page that
:api:`explains our collision detection <gma.collisions>`


Separating Concerns
-------------------

The Gamma framework aims to disconnect the game logic from the visual logic.
We have  achieved this by making an interface that sits between Gamma and an
arbitary rendering engine. This interface is collectively referred to as the
``Render Helpers``. Theoretically we can define rendering helpers for many
rendering engines, and perhaps even non-webgl engines.
At this point we only have Render Helpers that use GLGE.
You can find more about these :ref:`here <renderHelpers>`.


Limitations for Simplicity
--------------------------

Gamma was designed to be with two main limitations to keep the code simple

* Entities can only move in 2D space
* Everything is a square

Below is the list of places in the Gamma codebase that makes these assumptions

* The entire collision detection assumes we don't need to look at the ``z`` axis
  , and that everything is a square

  * :metho:`gma.collisions.detectCollisions`,
    :metho:`gma.collisions.factories.findCollisions`,
    :metho:`gma.collisions.factories.findGround`,
    :metho:`gma.collisions.factories.findBlockers`

* We only supply directional :api:`constants <gma.constants>` that represent
  2D directions,
  (:constant:`LEFT`, :constant:`RIGHT`, :constant:`FALLING`, :constant:`JUMPING`)

* :metho:`gma.renderHelper.setLocation` assumes entities don't have a ``z``
  property.

* :api:`gma.moveable` assumes it only needs to keep track of vertical and
  horizontal state (:prop:`gma.moveable.xState` and :prop:`gma.moveable.yState`)

* :api:`gma.moveable` also has functions that change the position of an entity,
  and they all assume we only need to update it's :prop:`gma.moveable.x` and
  :prop:`gma.moveable.y` properties

   * :metho:`gma.moveable.updatePositions`,
     :metho:`gma.moveable.animate`,
     :metho:`gma.moveable.getMovement`
   * This also means everything that inherits from :api:`gma.moveable` have the
     same limitations.

* :api:`gma.shapes.rectangle` has a couple of functions that don't care about
  the ``z`` axis.

   * :metho:`gma.shapes.rectangle.setBottomLeft` and
     :metho:`gma.shapes.rectangle.setPointsAndEdges`

* :api:`gma.shapes.rectangle` is the only object that provides any "shape"
  functionality.


Functionality through tags
--------------------------

Gamma uses a very simple tags system to provide the ability to specify
particular functionality on entities. This is explained in further detail
on :ref:`this page <tags>`.
