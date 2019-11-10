

.. api:: gma.moveable


.. api:: moveable



gma.moveable
============


    Provides functionality for a moveable shape



    =================== ===================================================================================================================
    Package             gma/entities/moveable
    Inheritance chain   :api:`gma.shapes.rectangle`
    Descendants         :api:`gma.character`, :api:`gma.enemy`, :api:`gma.platformEnemy`, :api:`gma.jumpingEnemy`, :api:`gma.patrolEnemy`
    =================== ===================================================================================================================




Tags
----


*shape*, *moveable*





Properties
----------


.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:prop:`points <gma.shapes.rectangle.points>`, :prop:`edges <gma.shapes.rectangle.edges>`, :prop:`width <gma.shapes.rectangle.width>`, :prop:`height <gma.shapes.rectangle.height>`, :prop:`depth <gma.shapes.rectangle.depth>`, :prop:`z <gma.shapes.rectangle.z>`, :prop:`x <gma.shapes.rectangle.x>`, :prop:`y <gma.shapes.rectangle.y>`, :prop:`centre <gma.shapes.rectangle.centre>`, :prop:`left <gma.shapes.rectangle.left>`, :prop:`right <gma.shapes.rectangle.right>`, :prop:`top <gma.shapes.rectangle.top>`, :prop:`bottom <gma.shapes.rectangle.bottom>`, :prop:`yOffset <gma.shapes.rectangle.yOffset>`, :prop:`xOffset <gma.shapes.rectangle.xOffset>`, :prop:`type <gma.shapes.rectangle.type>`, :prop:`alive <gma.shapes.rectangle.alive>`, :prop:`solid <gma.shapes.rectangle.solid>`, :prop:`tags <gma.shapes.rectangle.tags>`





.. _gma.moveable.yState:


.. prop:: gma.moveable.yState


**yState**
           
    Flag saying whether character is jumping, falling or neither
        
    +---------+---------------------+
    | Type    | :api:`gma.constant` |
    +---------+---------------------+
    | Default | :constant:`FALLING` |
    +---------+---------------------+





.. _gma.moveable.xState:


.. prop:: gma.moveable.xState


**xState**
           
    Flag saying whether character is going left, right or neither
        
    +---------+---------------------+
    | Type    | :api:`gma.constant` |
    +---------+---------------------+
    | Default | :constant:`STILL`   |
    +---------+---------------------+





.. _gma.moveable.lastXState:


.. prop:: gma.moveable.lastXState


**lastXState**
           
    Flag saying what direction character was going last before becoming horizontally still
        
    +---------+---------------------+
    | Type    | :api:`gma.constant` |
    +---------+---------------------+
    | Default | self.xState         |
    +---------+---------------------+





.. _gma.moveable.velocity:


.. prop:: gma.moveable.velocity


**velocity**
           
    Number representing how fast the character is moving vertically
        
    +---------+--------+
    | Type    | Number |
    +---------+--------+
    | Default | 0      |
    +---------+--------+





.. _gma.moveable.jumpVelocity:


.. prop:: gma.moveable.jumpVelocity


**jumpVelocity**
           
    Number representing the initial velocity of a jump
        
    +---------+--------+
    | Type    | Number |
    +---------+--------+
    | Default | 4      |
    +---------+--------+






Methods
-------


.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:metho:`setPointsAndEdges <gma.shapes.rectangle.setPointsAndEdges>`, :metho:`setCentre <gma.shapes.rectangle.setCentre>`, :metho:`setBottomLeft <gma.shapes.rectangle.setBottomLeft>`, :metho:`xOf <gma.shapes.rectangle.xOf>`, :metho:`yOf <gma.shapes.rectangle.yOf>`, :metho:`toString <gma.shapes.rectangle.toString>`, :metho:`collided <gma.shapes.rectangle.collided>`, :metho:`collided__deathtouch <gma.shapes.rectangle.collided__deathtouch>`




.. index:: pair: moveable; getMovement()

.. _gma.moveable.getMovement:


.. metho:: gma.moveable.getMovement


**getMovement** (moveAmount) -> Amount to move as [x, y]
    | Looks at the character's state and determines how far it should move
    | This result will then be checked for collisions and may be modified
    | If the character is jumping :
    
    * Keep going up if haven't reached targetY
    * else set vertical state to FALLING
    
    | If we're falling, then we go down
    | If horizontal state is not STILL, then we add horizontal movement.
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +================+===========+=====================================================+
    | moveAmount     | Number    | The amount the character should move                |
    +----------------+-----------+-----------------------------------------------------+





.. index:: pair: moveable; animate()

.. _gma.moveable.animate:


.. metho:: gma.moveable.animate


**animate** (delta, manager)
    | Changes character's position according to it's state
    | First it asks getMovement how much we should move
    | Then it determines how far we can move given the environment
    | It will then change the state of the character accordingly
    | It will then determine if the character is on top of ground
    | and set vertical state to FALLING or STILL accordingly
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +============+============================+========================================+
    | delta      | Number                     | Time since last animation              |
    +------------+----------------------------+----------------------------------------+
    | manager    | :api:`gma.manager`         |                                        |
    +------------+----------------------------+----------------------------------------+





.. index:: pair: moveable; findGround()

.. _gma.moveable.findGround:


.. metho:: gma.moveable.findGround


**findGround** (manager)
    Finds any ground the character is on and changes state accordingly
    

    



    +---------------------------------------------------------------------------------+
    | Parameters                                                                      |
    +========================+========================================================+
    | manager                | :api:`gma.manager`                                     |
    +------------------------+--------------------------------------------------------+





.. index:: pair: moveable; updatePositions()

.. _gma.moveable.updatePositions:


.. metho:: gma.moveable.updatePositions


**updatePositions** (vector)
    Changes it's position, centre, points and edges.
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +=========+=========+==============================================================+
    | vector  | [x, y]  | Vector representing the amount character can move            |
    +---------+---------+--------------------------------------------------------------+





.. index:: pair: moveable; getRotation()

.. _gma.moveable.getRotation:


.. metho:: gma.moveable.getRotation


**getRotation** ( ) -> Number
    Gets rotation in radians
    

    







.. index:: pair: moveable; kill()

.. _gma.moveable.kill:


.. metho:: gma.moveable.kill


**kill** ( )
    Kills the entity. Should be overwritten to do something useful.
    

    







