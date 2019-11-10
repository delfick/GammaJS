Adding Lights
=============

To add a light to your level you can specify options under the ``light`` label
inside your level specification. For example:

.. code-block:: javascript

   var myLevel = {
        light : {
            myLight : {
                //options
            }
        }
    };


We will define a point (directional) light. The light is position 5 units above
and 20 units in front of the character (therefore, an offset of [0,5,20]).
We must also rotate it 180 degrees (1.54 radians) to point into the scene
(and at the character). The light will emit a white light:

.. code-block:: javascript

    var myLevel = {
        light : {
            myLight : {
                type : GLGE.L_POINT,
                rotY : 1.54,
                color    : "#fff",
                attached : ['character', 0,5,20]
            }
        }
    };

The :ref:`level specification topic <levelSpecs>` has more information about
:ref:`adding and configuring lights <lights>`.

What's next?
------------

In the next section we will :doc:`learn how to apply a texture <textures>`.
