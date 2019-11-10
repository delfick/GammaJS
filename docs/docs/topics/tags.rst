.. _tags:

Tags
====

Gamma uses ``tags`` to control the behaviour and other attributes of entities.
Every entity, (i.e. anything that is a descendant of :api:`gma.shapes.rectangle`),
has a property :prop:`gma.shapes.rectangle.tags` which is a :term:`hash`.

An entity is considered to have a particular tag if the tag-name can be found in
the :prop:`gma.shapes.rectangle.tags` property and it has a truthy value.

.. code-block:: javascript

    if (myEntity.tags.fast) {
        // This entity has the 'fast' tag.
    }

Gamma provides and knows about many tags which control the behaviour of
:doc:`enemies <enemy>` and :doc:`platforms <platform>` such as *deathtouch*,
*jumping*, and *weakhead*.

.. note:: When we refer to `behaviour` here, we mean both movement
    rules/behaviour, what happens when collisions occur and other attributes
    of entities.

Setting tags
++++++++++++

There are two ways you can set tags on an entity:

Adding a tag to the created entity
----------------------------------

When we have already created an entity, then to give it a tag, we set it to
``true`` on the :prop:`gma.shapes.rectangle.tags` property:

.. code-block:: javascript

    var myShape = gma.shapes.rectangle({x:0, y:0, width:1, height:1});

    //Give the entity "deathly", "scared" and "psycho" tags.
    myShape.tags.deathly = true;
    myShape.tags.scared = true;
    myShape.tags.psycho = true;

Listing tags when instantiating the entity
------------------------------------------

You can also give an entity some tags when you create it. Specify tags by
providing the tag as an array of strings. The entity will set each listed tag
to ``true`` in the :prop:`gma.shapes.rectangle.tags` list.

.. code-block:: javascript

    var myShape = gma.shapes.rectangle({
        x:0, y:0, width:1, height:1,
        tags : ['deathly', 'scared', 'psycho']
    });

    // Print tags to the console
    console.log(myShape.tags);

    // The console will output:
    // {deathly : true, scared : true, psycho : true, shape : true}

    // ::NOTE:: gma.shapes.rectangle will set a tag of "shape" on the entity


Removing tags
+++++++++++++

You can remove tags by using the javascript `delete` keyword.

.. code-block:: javascript

    var myShape = gma.shapes.rectangle({
        x:0, y:0, width:1, height:1,
        tags : ['deathly', 'scared', 'psycho']
    });

    // Checking it exists at all before deleting it is good practise
    if (myShape.tags.deathly) {
        delete myShape.tags.deathly;
    }

    // Print tags to the console
    console.log(myShape.tags);

    // The console will output:
    // {scared : true, psycho : true, shape : true}
