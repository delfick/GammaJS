﻿.. _appearance:

Appearance
==========

Specifying the 3D object which is rendered to represent an entity is done
through using templates. Gamma provides 3 different templates which can be used
to specify a 3D object to be rendered.

:api:`gma.meshTemplate` to specify a mesh internally.

:api:`gma.glgeIDTemplate` to specify objects found in an external xml file.

:api:`gma.colladaTemplate` to specify an external collada file.

.. note:: To use a template, you must require the ``gma/utils/render`` package

.. note:: Gamma only provides rendering support for `GLGE <http://www.glge.org/>`_,
    but feel free to see the
    :ref:`explanation of render helpers and templates <renderHelpers>`
    to find out how to add support for other rendering engines.

MeshTemplate
------------

This template is useful where an object's mesh is stored internally.

When you define a :api:`gma.meshTemplate`, you need to specify a ``mesh``
and either a ``material`` or a ``texture``.

Material
++++++++

Material can be specified if you wish to have a simple color for the surface of
your mesh. This is done using a hexadecimal value as shown bellow:

.. code-block:: javascript

    var thing = gma.meshTemplate({
        mesh : myMesh,
        material : {color : '#090'}
    };

You can look at the ``set_*`` methods :glge:`here <Material>` to see what
options you can set on the material.

Texture
+++++++

Texture can be specified if you wish to have an image mapped on to the surface
of your mesh. This is done by specifying the source of where the image is stored.

.. code-block:: javascript

    var thing = gma.meshTemplate({
        mesh : myMesh,
        texture : {src : 'cloud.png'}
    });

The texture by default will loop for every unit of the entities' height, width
and depth. You can change this by specifying the ``repeatX`` and ``repeatY`` on
the texture.

.. code-block:: javascript

    var thing = gma.meshTemplate({
        mesh : myMesh,
        texture : {
            src : 'cloud.png',
            repeatX : 0.2,
            repeatY : 0.2
        }
    });

You can look at the ``set_*`` methods :glge:`here <Texture>` to see what options
you can set on the texture.

Mesh
++++

Gamma provides a cube mesh which can be used to specify a simple cube in
:prop:`gma.gma.unitCubeInfo`, which is ideal for platforms.

.. code-block:: javascript

    var aCube = gma.meshTemplate({
        mesh : gma.unitCubeInfo.mesh,
        material : myMaterial
    });

Alternatively you could create your own mesh. Eg:

.. code-block:: javascript

    var myMesh = {
        // An array of the x, y,z coordinates of each vertex
        positions : [],

        // An array of the x,y,z coordinates for the normal for each vertex
        normals : [],

        // An array of the x,y UV coordinates for each vertex
        UV : [],

        // An array of specifying which vertexes go together to make each face
        faces : []
    });

    var thingUsingMyMesh = gma.meshTemplate({
        mesh : myMesh,
        material : myMaterial
    });

Look at the ``set_*`` methods over :glge:`here <Mesh>` for more options that you
can set on the mesh.

GLGE ID Template
----------------

The GLGE rendering engine provides the ability to define an object using xml.
Gamma allows you to include these xml files by giving
:prop:`gma.manager.resources` a list of paths to the xml you want to include.

For example, say you have the following xml file

.. code-block:: xml

    <?xml version="1.0" ?>
    <glge>
        <mesh id="box">
                <positions>1.000000,1.000000,-1.000000,1.000000,-1.000000,-1.000000,-1.000000,-1.000000,-1.000000,-1.000000,1.000000,-1.000000,1.000000,0.999999,1.000000,-1.000000,1.000000,1.000000</positions>
                        <normals>0.000000,0.000000,-1.000000,0.000000,0.000000,-1.000000,0.000000,0.000000,-1.000000,0.000000,0.000000,-1.000000,0.000000,-0.000000,1.000000,0.000000,-0.000000,1.000000,0.000000</normals>
                                <uv1>0.000000,0.000000,1.000000,0.000000,1.000000,1.000000,0.000000,1.000000,0.000000,0.000000,1.000000</uv1>
            <faces>0,1,2,0,2,3,4,5,6,4,6,7,8,9</faces>

        </mesh>
        <material id="red" color="#900"/>
        <object id="redcube" mesh="#box" material="#red" />
    </glge>

You can reference an object specified within an xml file, such as the redcube
object shown above as a template for rendering an object by simply doing the
following:

.. code-block:: javascript

   var myRedCube = gma.glgeIdTemplate({id : "redcube"})

.. note:: You can use :api:`gma.glgeIDTemplate` objects to get anything from the
    xml, just simply create one and call it's
    :metho:`gma.glgeIDTemplate.defineInstance` function.

Collada Template
----------------

`Collada <https://collada.org>`_ is open standard xml schema to define a model.
Most 3D modelling applications support exporting models in this format (.dae).

You can specify a collada file as a template for rendering an object by using
:api:`gma.colladaTemplate`. All you need to do is specify a ``collada``
property that has a ``document`` property which defines where the collada file
is stored.

For example,

.. code-block:: javascript

   var myGorilla = gma.colladaTemplate({
       collada : {
           document : 'mygorilla.dae'
       }
   });

Size of the rendered Object
---------------------------

When you specify an entities' dimensions, the rendered object used for this
object is scaled by these dimensions.

However, this will only produce the desired results when the object being scaled
is unit size to begin with. Unfortunately it not currently possible to determine
the size of the object being rendered, and so the programmer must manually
specify how much to scale the object before it is unit size.

For example, say you have a collada object that is 2 units high by 4 units wide.
Then it must be scaled by half vertically, and by a quarter horizontally, before
it can be accurately scaled to the size of the entity.
To specify this, we simply specify :prop:`gma.baseTemplate.xScale` and
:prop:`gma.baseTemplate.yScale` when we create our templateHelper.

For example,

.. code-block:: javascript

   var myFatGorilla = gma.colladaTemplate({
       document {
           src : 'mygorilla.dae'
       },
       xScale : 0.25,
       yScale : 0.5
   });

The :api:`gma.baseTemplate` allows you to specify
:prop:`gma.baseTemplate.xScale`,
:prop:`gma.baseTemplate.yScale`,
:prop:`gma.baseTemplate.zScale`,
:prop:`gma.baseTemplate.yRot`,
:prop:`gma.baseTemplate.xRot`,
:prop:`gma.baseTemplate.zRot`,
:prop:`gma.baseTemplate.xOffset`,
:prop:`gma.baseTemplate.yOffset` and
:prop:`gma.baseTemplate.zOffset` for the purpose of such normalisation.
