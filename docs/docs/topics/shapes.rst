.. _definingShapes:

Shapes
======

One of the fundamental aspects of Gamma is that anything that can be interacted
with has a bounding box that is used for collision detection. For now, Gamma
only supports rectangular bounding boxes, however this may change in the future.

To provide the functionality required for a bounding box, we have a set of
functions and properties that can be added to your object using
:api:`gma.shapes.rectangle`.

.. note:: Gamma provides several entity classes out of the box that use
    :api:`gma.shapes.rectangle`. Look at the descendants list on that api page
    for a full list of such classes.

Creating a rectangle
--------------------

.. _rectangle:

To specify a rectangle, you need to be able to determine it's width, height and
position using the available properties. Gamma allows you to specify this in
several ways, as outlined below. If these aspects can't be determined, then the
rectangle can't be made and :api:`gma.shapes.rectangle` will return ``null``.

Specifying width and horizontal position
++++++++++++++++++++++++++++++++++++++++

Any of the following combinations will allow you to specify a width and
horizontal position, where ``x`` is the horizontal co-ordinate of the centre of
the rectangle, ``left`` and ``right`` are the horizontal extremes of the
rectangle and ``width`` is it's absolute width.

 * ``width`` and ``right``
 * ``width`` and ``left``
 * ``width`` and ``x``
 * ``left`` and ``right``
 * ``x`` and ``left``
 * ``x`` and ``right``

Specifying height and vertical position
+++++++++++++++++++++++++++++++++++++++

Any of the following combinations will allow you to specify a height and
vertical position, where ``y`` is the vertical co-ordinate of the centre of the
rectangle, ``top`` and ``bottom`` are the vertical extremes of the rectangle and
``height`` is it's absolute height.

 * ``height`` and ``bottom``
 * ``height`` and ``top``
 * ``height`` and ``y``
 * ``top`` and ``bottom``
 * ``y`` and ``top``
 * ``y`` and ``bottom``

Examples
++++++++

.. code-block:: javascript

	// top, bottom, right and left
	gma.platform({left:1, right:3, top:3, bottom:2});

	// (top or bottom), (left or right), height and width
	gma.platform({bottom:1, right:3, height:1, width:2});
	gma.platform({bottom:1, left:1,  height:1, width:2});
	gma.platform({top:2,    right:3, height:1, width:2});
	gma.platform({top:2,    left:1,  height:1, width:2});

	// (top or bottom), left, right and height
	gma.platform({bottom:1, right:3, left:1, height:1});
	gma.platform({top:2,    right:3, left:1, height:1});

	// (left or right), top, bottom and width
	gma.platform({left:1,  bottom:1, width:2});
	gma.platform({right:3, bottom:1, width:2});

	// centre, width and height
	gma.platform({ centre:[2,1.5], width:2, height:1 });

	// x, y, width and height
	gma.platform({ x:2, y:1.5, width:2, height:1 });

Specifying Points
+++++++++++++++++

An *alternative* way of specifying a rectangle is to specify points that make up
the corners of the rectangle. This is done by specifying ``points`` with an
array of [x,y] co-ordinates. How many points you supply and in what order is up
to you, as long as you have at least two diagonally opposite corners, then it
will work.

Examples
++++++++

For example, creating a :api:`gma.platform`, which uses :api:`gma.shapes.rectangle`.

.. code-block:: javascript

	// All four corners
	gma.platform({ points:[[1,1],[3,1],[3,2],[1,2]] });

	// 2 opposite corners
	gma.platform({ points:[[1,1],[3,2]] });
	gma.platform({ points:[[3,1],[1,2]] });
