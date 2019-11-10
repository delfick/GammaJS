

.. api:: gma.character


.. api:: character



gma.character
=============


    Provides a character object



    =================== ====================================================
    Package             gma/entities/character
    Inheritance chain   :api:`gma.shapes.rectangle` >> :api:`gma.moveable`
    =================== ====================================================




Tags
----


*shape*, *moveable*, *character*





Properties
----------


.. admonition:: Inherited from :api:`gma.moveable`

	:prop:`yState <gma.moveable.yState>`, :prop:`xState <gma.moveable.xState>`, :prop:`lastXState <gma.moveable.lastXState>`, :prop:`velocity <gma.moveable.velocity>`, :prop:`jumpVelocity <gma.moveable.jumpVelocity>`

.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:prop:`points <gma.shapes.rectangle.points>`, :prop:`edges <gma.shapes.rectangle.edges>`, :prop:`width <gma.shapes.rectangle.width>`, :prop:`height <gma.shapes.rectangle.height>`, :prop:`depth <gma.shapes.rectangle.depth>`, :prop:`z <gma.shapes.rectangle.z>`, :prop:`x <gma.shapes.rectangle.x>`, :prop:`y <gma.shapes.rectangle.y>`, :prop:`centre <gma.shapes.rectangle.centre>`, :prop:`left <gma.shapes.rectangle.left>`, :prop:`right <gma.shapes.rectangle.right>`, :prop:`top <gma.shapes.rectangle.top>`, :prop:`bottom <gma.shapes.rectangle.bottom>`, :prop:`yOffset <gma.shapes.rectangle.yOffset>`, :prop:`xOffset <gma.shapes.rectangle.xOffset>`, :prop:`type <gma.shapes.rectangle.type>`, :prop:`alive <gma.shapes.rectangle.alive>`, :prop:`solid <gma.shapes.rectangle.solid>`, :prop:`tags <gma.shapes.rectangle.tags>`





.. _gma.character.score:


.. prop:: gma.character.score


**score**
           
    Holds a score counter
        
    +------+--------+
    | Type | Number |
    +------+--------+






Methods
-------


.. admonition:: Inherited from :api:`gma.moveable`

	:metho:`getMovement <gma.moveable.getMovement>`, :metho:`animate <gma.moveable.animate>`, :metho:`findGround <gma.moveable.findGround>`, :metho:`updatePositions <gma.moveable.updatePositions>`, :metho:`getRotation <gma.moveable.getRotation>`, :metho:`kill <gma.moveable.kill>`

.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:metho:`setPointsAndEdges <gma.shapes.rectangle.setPointsAndEdges>`, :metho:`setCentre <gma.shapes.rectangle.setCentre>`, :metho:`setBottomLeft <gma.shapes.rectangle.setBottomLeft>`, :metho:`xOf <gma.shapes.rectangle.xOf>`, :metho:`yOf <gma.shapes.rectangle.yOf>`, :metho:`toString <gma.shapes.rectangle.toString>`, :metho:`collided__deathtouch <gma.shapes.rectangle.collided__deathtouch>`




.. index:: pair: character; jump()

.. _gma.character.jump:


.. metho:: gma.character.jump


**jump** (e)
    | Makes character ready for jumping
    | It will only set character to jumping if it's in the STILL state
    | It will also set self.targetY to it's current y plus it's jumpHeigt
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +=======+================+=========================================================+
    | e     | Event          | Keyboard event object                                   |
    +-------+----------------+---------------------------------------------------------+





.. index:: pair: character; move()

.. _gma.character.move:


.. metho:: gma.character.move


**move** (direction, e)
    Changes character's horizontal state
    

    



    +------------------------------------------------------------------------------------------------------+
    | Parameters                                                                                           |
    +===========+=====================+====================================================================+
    | direction | :api:`gma.constant` | gma.constant representing whether character is going left or right |
    +-----------+---------------------+--------------------------------------------------------------------+
    | e         | Event               | Keyboard event object                                              |
    +-----------+---------------------+--------------------------------------------------------------------+





.. index:: pair: character; collided()

.. _gma.character.collided:


.. metho:: gma.character.collided


**collided** (where, focus, focusSide, focusVector)
    | Collided function for character
    | Determines if we hit a collectable and what to do with it
    

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





.. index:: pair: character; collided__pickupCollectable()

.. _gma.character.collided__pickupCollectable:


.. metho:: gma.character.collided__pickupCollectable


**collided__pickupCollectable** (where, focus, focusSide, focusVector)
    Collision function for hitting a collectable
    

    



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





