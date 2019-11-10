.. _levelParsers:

Level Parser
============

If you need to extend or modify the level parser -- or are, perhaps, simply
curious -- this section describes how the level parser works.

When a Gamma :api:`manager <gma.manager>` loads a level, it parses the level
specifications with it's :prop:`gma.manager.levelParser` object.
The :api:`gma.levelParser` is designed to
**create gamma objects from the level specification object**.
By default the level parser object will be an instance of :api:`gma.levelParser`.

Level parsing begins with the
:metho:`processLevel(level) <gma.levelParser.processLevel>`
method which does the following:

* Check to see if the level has been previously processed

    * If it has, then return the level, parsing the level stops here

* Set any defaults on the level using :metho:`gma.levelParser.preProcess`

* Process the level

Determining if a level is already processed
-------------------------------------------

The level parser will consider a level as already processed if it has a property
on it called ``processed``, which is set to ``true``.

The levelParser will ensure this property is set to ``true`` on the level once
it has been processed.

Pre-Processing the level
------------------------

The :metho:`gma.levelParser.preProcess` function serves two purposes :

Expand Replicate With
+++++++++++++++++++++

Firstly, the :metho:`gma.utils.expandReplicateWith` method is used to expand
the level specification where the ``replicateWith`` key has been used.
See :ref:`ReplicateWith <replicateWith>` in the level creation topic.

Set up all necessary defaults on the level
++++++++++++++++++++++++++++++++++++++++++

Secondly set up defaults for a level's light, camera, entities and spawn
location. This is done using :metho:`gma.levelParser.default_light`,
:metho:`gma.levelParser.default_camera`,
:metho:`gma.levelParser.default_entities` and
:metho:
properties.

This function will also initialise the following properties:

level.removed
*************

This list is used by :metho:`gma.manager.twitch` when it calls
:metho:`gma.manager.removeDead`, which then uses it to store references to any
entities that have died with a ``reincarnate`` tag.

:metho:`gma.manager.loadLevel` uses this list of `reincarnatable` enemies to set
their status back to ``alive`` if when the level is reloaded.

level.following
***************

This is a :term:`dictionary` that holds any item that specifies it follows
another item. Currently only the light and camera may specify this, and they
are limited to following the character.

The dictionary is then used by :metho:`gma.manager.loadLevel`, which uses the
information in calls to :metho:`gma.sceneHelper.attach` on the manager's
:prop:`gma.manager.sceneHelper`.

level.levelExtras
*****************

References to any level specific items (currently, just lights and camera) that
have been added the the rendered scene. This list is maintained so that when
:metho:`gma.manager.clearLevel` is called, it knows what extra items in the
current scene belong to the current level and must be removed. (This allows
lights and other objects to be permanently added to the scene, regardless of
the currently level.)

Processing a level
------------------

The levelParser is designed such that processing each item in the level is done
independently of other items. This is accomplished by a suite of ``validate_*``
and ``process_*`` functions (the star represents the property on the level that
these functions will operate on). Gamma provides processing functions for
entities, light, camera, other, utility, following, template, removed and
levelExtras.

For example to process entities in a level specification,

.. code-block:: javascript

    var myLevel = {
        entities : [
            {left:19, right:30, top:9, height:3}
        ]
    };

Gamma provides the following functions in :api:`gma.levelParser`:

.. code-block:: javascript

    self.validate_entities = function(manager, key, value, level) {
    ...
    };

    self.process_entities = function(manager, key, value, level) {
    ...
    }

    self.default_entities = function(manager, key, value, level) {
    ...
    }

Arguments to validate and process functions
+++++++++++++++++++++++++++++++++++++++++++

Each validate and process function will receive, in this order, a ``manager``
object, the ``key`` of the property being processed, the ``value`` of the
property being processed, and the ``level`` object being processed.

Changes made to the level object are permanent and cannot be reversed.

Validate function
+++++++++++++++++

The validate function checks whether it is possible to create a gamma object
with the properties specified. These functions will simply return a Boolean
saying whether the information is valid or not.

This function is allowed to transform the data to be valid for processing.

Process function
++++++++++++++++

The process function will turn each object specification into an actual gamma
object. This way :metho:`gma.manager.loadLevel` does not need to worry about
whether the objects in the level are gamma objects or just specifications.

.. _levelParserPreProcess:

Default function
++++++++++++++++

The default function is optional. It is used by
:metho:`gma.levelParser.preProcess` to set up a default for the level where one
is not specified.


Processing a Custom Type
------------------------

You can create you own type of object in the level parser. For example, say we
want to make the levelParser aware of a ``skybox`` property on the level, then
all we need to do is create ``validate_skybox`` and ``process_skybox`` functions.
Then optionally create a ``default_skybox`` function and override
:metho:`gma.levelParser.preProcess` such that it is used.

.. code-block:: javascript

    var myLevelParser = (function() {
        var self = gma.levelParser();

        var oldPreProcess = self.preProcess;
        self.preProcess = function(level) {
            level = oldPreProcess(level);

            level.skybox = level.skybox || self.default_skybox();
        };

        self.validate_skybox(manager, key, value, level) {
            //validate the information given for the skybox property here
        };

        self.process_skybox(manager, key, value, level) {
            //Do any necessary processing/transformation to the information given for the skybox here
        };
    })();

Then we just set this new levelParser on the manager, and then when we use
:metho:`gma.manager.loadLevel`, it will be aware of the skybox property and
handle it as you have specified.

.. note:: If the levelparser can't find an associated validate and/or process
    function for a property, it will use the generic
    :metho:`gma.levelParser.validate_other` and
    :metho:`gma.levelParser.process_other` methods.
