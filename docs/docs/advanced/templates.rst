.. _renderHelpers:

Render Helpers and Templates
============================

This page explains how Gamma uses :api:`gma.renderHelper` to provide the link
between Gamma entities and the rendering engine.

Everything that is rendered in Gamma is found inside the ``entities`` or
``levelExtras`` property of the current level. The content of the ``entities``
list doesn't matter, as long as each `entity` has a ``helper`` property that
is an instance of :api:`gma.renderHelper`, and that the `render helper` has
a :prop:`gma.renderHelper.template` property set to a descendant of
:api:`gma.baseTemplate`. These `render helpers` are used to provide the visual
representation to the `scene helper`.

.. note:: See :ref:`appearance` for more information on templates

As a part of processing a level, in the
:metho:`gma.levelParser.process_entities` method, the
:prop:`gma.manager.levelParser` will go through all the entities in the level
and use :metho:`gma.manager.prepareEntity` to give them each a
:api:`gma.renderHelper`.

These render helper objects are responsible for ensuring that the visual
representation of the entity it belongs to has the correct size and position
and is added to the current :prop:`gma.manager.sceneHelper`.
The render helper also maintains a cache of the object specifying this
representation.

Registering with the SceneHelper
++++++++++++++++++++++++++++++++

As a part of loading a level, :metho:`gma.manager.loadLevel` will go through
the ``entities`` list on the current level and ask the
:prop:`gma.manager.sceneHelper` to add each entity's ``helper`` object.

This will cause the :api:`gma.sceneHelper` to call the render helper's
:metho:`gma.renderHelper.addTo` method with a container that it can add the
visual representation to.

Maintaining size and position
+++++++++++++++++++++++++++++

As part of the :term:`Game Loop`, the manager's :prop:`gma.manager.sceneHelper`
is asked to render the scene using it's :metho:`gma.sceneHelper.render` method.
This method will first update all the objects specific to the rendering engine
using :metho:`gma.sceneHelper.setRenderedLocations` and then use ask the
rendering engine to render everything.

The :metho:`gma.sceneHelper.setRenderedLocations` method will go through each
entity on the current level and call :metho:`gma.renderHelper.setLocation` on
each entity's render helper. This method will get the object that represents
the entity and make sure it accurately represents the size and position of the
entity.

.. note:: The :metho:`gma.sceneHelper.setRenderedLocations` method is also
    responsible for ensuring anything registered as being
    :ref:`attached <attached>` to something else is moved when that entity
    is moved.

Providing a cache
+++++++++++++++++

To get the rendering specific object from a render helper, we call it's
:metho:`gma.renderHelper.getRenderedObj` method. This method will look for an
``_instance`` attribute on the render helper. If it does not have one, then it
will ask it's template (one is added as part of
:metho:`gma.manager.prepareEntity`) to give it an instance to work with by
calling it's :metho:`gma.baseTemplate.getInstance` method.

.. note:: You can override the template on the render helper just by setting
    it's ``_instance`` property.
