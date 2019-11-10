

.. api:: gma.enemy


.. api:: enemy



gma.enemy
=========


    Provides a base enemy object



    =================== ===========================================================================
    Package             gma/entities/enemy
    Inheritance chain   :api:`gma.shapes.rectangle` >> :api:`gma.moveable`
    Descendants         :api:`gma.platformEnemy`, :api:`gma.jumpingEnemy`, :api:`gma.patrolEnemy`
    =================== ===========================================================================




Tags
----


*shape*, *moveable*, *enemy*





Properties
----------


.. admonition:: Inherited from :api:`gma.moveable`

	:prop:`yState <gma.moveable.yState>`, :prop:`xState <gma.moveable.xState>`, :prop:`lastXState <gma.moveable.lastXState>`, :prop:`velocity <gma.moveable.velocity>`, :prop:`jumpVelocity <gma.moveable.jumpVelocity>`

.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:prop:`points <gma.shapes.rectangle.points>`, :prop:`edges <gma.shapes.rectangle.edges>`, :prop:`width <gma.shapes.rectangle.width>`, :prop:`height <gma.shapes.rectangle.height>`, :prop:`depth <gma.shapes.rectangle.depth>`, :prop:`z <gma.shapes.rectangle.z>`, :prop:`x <gma.shapes.rectangle.x>`, :prop:`y <gma.shapes.rectangle.y>`, :prop:`centre <gma.shapes.rectangle.centre>`, :prop:`left <gma.shapes.rectangle.left>`, :prop:`right <gma.shapes.rectangle.right>`, :prop:`top <gma.shapes.rectangle.top>`, :prop:`bottom <gma.shapes.rectangle.bottom>`, :prop:`yOffset <gma.shapes.rectangle.yOffset>`, :prop:`xOffset <gma.shapes.rectangle.xOffset>`, :prop:`type <gma.shapes.rectangle.type>`, :prop:`alive <gma.shapes.rectangle.alive>`, :prop:`solid <gma.shapes.rectangle.solid>`, :prop:`tags <gma.shapes.rectangle.tags>`






Methods
-------


.. admonition:: Inherited from :api:`gma.moveable`

	:metho:`animate <gma.moveable.animate>`, :metho:`findGround <gma.moveable.findGround>`, :metho:`updatePositions <gma.moveable.updatePositions>`, :metho:`getRotation <gma.moveable.getRotation>`, :metho:`kill <gma.moveable.kill>`

.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:metho:`setPointsAndEdges <gma.shapes.rectangle.setPointsAndEdges>`, :metho:`setCentre <gma.shapes.rectangle.setCentre>`, :metho:`setBottomLeft <gma.shapes.rectangle.setBottomLeft>`, :metho:`xOf <gma.shapes.rectangle.xOf>`, :metho:`yOf <gma.shapes.rectangle.yOf>`, :metho:`toString <gma.shapes.rectangle.toString>`, :metho:`collided__deathtouch <gma.shapes.rectangle.collided__deathtouch>`




.. index:: pair: enemy; getMovement()

.. _gma.enemy.getMovement:


.. metho:: gma.enemy.getMovement


**getMovement** (moveAmount) -> Amount to move as [x, y]
    | Enemy getMovement will first call determineState before doing super.getMovement
    | The enemy is the same as the character, except it
    | determines it's own next state, rather than the player
    

    **Overrides** :metho:`gma.moveable.getMovement <gma.moveable.getMovement>`
    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +================+===========+=====================================================+
    | moveAmount     | Number    | The amount the character should move                |
    +----------------+-----------+-----------------------------------------------------+





.. index:: pair: enemy; determineState()

.. _gma.enemy.determineState:


.. metho:: gma.enemy.determineState


**determineState** (moveAmount, manager)
    | Determine the state of the enemy for the next movement
    | - Calls behaviour__jumping if it has jumping tag
    | - Calls behaviour__patrolling if it has patrolling tag
    | - Calls behaviour__platformer if it has platformer tag
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +============+=====================+===============================================+
    | moveAmount | Number              | amount to move; based on delta from twitch    |
    +------------+---------------------+-----------------------------------------------+
    | manager    | :api:`gma.manager`  |                                               |
    +------------+---------------------+-----------------------------------------------+





.. index:: pair: enemy; collided()

.. _gma.enemy.collided:


.. metho:: gma.enemy.collided


**collided** (where, focus, focusSide, focusVector)
    | Enemy looks for rebound and weakhead tags as well as what super.collided looks for
    | It will also look for deathtouch, if enemy is still alive after all other checks
    

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





.. index:: pair: enemy; behaviour__jumping()

.. _gma.enemy.behaviour__jumping:


.. metho:: gma.enemy.behaviour__jumping


**behaviour__jumping** (moveAmount, manager)
    Makes enemy jump when touching ground
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +============+=====================+===============================================+
    | moveAmount | Number              | amount to move; based on delta from twitch    |
    +------------+---------------------+-----------------------------------------------+
    | manager    | :api:`gma.manager`  |                                               |
    +------------+---------------------+-----------------------------------------------+





.. index:: pair: enemy; behaviour__platformer()

.. _gma.enemy.behaviour__platformer:


.. metho:: gma.enemy.behaviour__platformer


**behaviour__platformer** (moveAmount, manager)
    Makes enemy turn around when reaching the edge of the platform it is currently on
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +============+=====================+===============================================+
    | moveAmount | Number              | amount to move; based on delta from twitch    |
    +------------+---------------------+-----------------------------------------------+
    | manager    | :api:`gma.manager`  |                                               |
    +------------+---------------------+-----------------------------------------------+





.. index:: pair: enemy; behaviour__patrolling()

.. _gma.enemy.behaviour__patrolling:


.. metho:: gma.enemy.behaviour__patrolling


**behaviour__patrolling** (moveAmount, manager)
    | Makes enemy patrol a range
    | Requires self.limitLeft and/or self.limitRight properties
    

    



    +----------------------------------------------------------------------------------+
    | Parameters                                                                       |
    +============+=====================+===============================================+
    | moveAmount | Number              | amount to move; based on delta from twitch    |
    +------------+---------------------+-----------------------------------------------+
    | manager    | :api:`gma.manager`  |                                               |
    +------------+---------------------+-----------------------------------------------+





.. index:: pair: enemy; collided__rebound()

.. _gma.enemy.collided__rebound:


.. metho:: gma.enemy.collided__rebound


**collided__rebound** (where, focus, focusSide, focusVector)
    Makes enemy turn around if it hits something
    

    



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





.. index:: pair: enemy; collided__weakhead()

.. _gma.enemy.collided__weakhead:


.. metho:: gma.enemy.collided__weakhead


**collided__weakhead** (where, focus, focusSide, focusVector)
    Makes enemy die when character hit it's top
    

    



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





