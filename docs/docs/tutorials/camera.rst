Customise the Camera
====================

Gamma creates a default camera which follows the character's movement and is 50
units in front of the character --- a ``z`` location of 50.

To change the camera in your level, you can specify options under the ``camera``
label in the level specification. You can only specify one camera in each level
specification. When a camera is specified in your level it will override the
default camera provided by Gamma.

The following specification is the equivalent of the default camera:

.. code-block:: javascript

   var myLevel = {
        camera : {
            locZ : 50,
            attached : ['character']
        }
    };

Lets specify a camera a little bit further away from the character, but always
a bit higher than it:

.. code-block:: javascript

   var myLevel = {
        camera : {
            locZ : 60,
            attached : ['character',0, 6]
        }
    };

What's next?
------------

In the next section we will :doc:`learn how to add some lights <lights>`.
