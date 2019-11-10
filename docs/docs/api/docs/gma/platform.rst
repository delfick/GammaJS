

.. api:: gma.platform


.. api:: platform



gma.platform
============


    Provides a base platform object



    =================== =============================
    Package             gma/entities/platform
    Inheritance chain   :api:`gma.shapes.rectangle`
    Descendants         :api:`gma.deathPlatform`
    =================== =============================




Tags
----


*shape*, *platform*





Properties
----------


.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:prop:`points <gma.shapes.rectangle.points>`, :prop:`edges <gma.shapes.rectangle.edges>`, :prop:`width <gma.shapes.rectangle.width>`, :prop:`height <gma.shapes.rectangle.height>`, :prop:`depth <gma.shapes.rectangle.depth>`, :prop:`z <gma.shapes.rectangle.z>`, :prop:`x <gma.shapes.rectangle.x>`, :prop:`y <gma.shapes.rectangle.y>`, :prop:`centre <gma.shapes.rectangle.centre>`, :prop:`left <gma.shapes.rectangle.left>`, :prop:`right <gma.shapes.rectangle.right>`, :prop:`top <gma.shapes.rectangle.top>`, :prop:`bottom <gma.shapes.rectangle.bottom>`, :prop:`yOffset <gma.shapes.rectangle.yOffset>`, :prop:`xOffset <gma.shapes.rectangle.xOffset>`, :prop:`type <gma.shapes.rectangle.type>`, :prop:`alive <gma.shapes.rectangle.alive>`, :prop:`solid <gma.shapes.rectangle.solid>`, :prop:`tags <gma.shapes.rectangle.tags>`






Methods
-------


.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:metho:`setPointsAndEdges <gma.shapes.rectangle.setPointsAndEdges>`, :metho:`setCentre <gma.shapes.rectangle.setCentre>`, :metho:`setBottomLeft <gma.shapes.rectangle.setBottomLeft>`, :metho:`xOf <gma.shapes.rectangle.xOf>`, :metho:`yOf <gma.shapes.rectangle.yOf>`, :metho:`toString <gma.shapes.rectangle.toString>`, :metho:`collided__deathtouch <gma.shapes.rectangle.collided__deathtouch>`




.. index:: pair: platform; collided()

.. _gma.platform.collided:


.. metho:: gma.platform.collided


**collided** (where, focus, focusSide, focusVector)
    Does super.collided checks and also looks for the deathtouch tag
    

    **Overrides** :metho:`gma.shapes.rectangle.collided <gma.shapes.rectangle.collided>`
    



    +-------------------------------------------------------------------------------------+
    | Parameters                                                                          |
    +=============+=====================+=================================================+
    | where       | :api:`gma.constant` | Side of this object that was collided with      |
    +-------------+---------------------+-------------------------------------------------+
    | focus       | object              | Thing we collided with                          |
    +-------------+---------------------+-------------------------------------------------+
    | focusSide   | :api:`gma.constant` | Side of the focus object that was collided with |
    +-------------+---------------------+-------------------------------------------------+
    | focusVector | [x,y]               | Amount focus is trying to move                  |
    +-------------+---------------------+-------------------------------------------------+





