

.. api:: gma.patrolEnemy


.. api:: patrolEnemy



gma.patrolEnemy
===============


    Provides an enemy that patrols a particular range



    =================== ========================================================================
    Package             gma/entities/enemy
    Inheritance chain   :api:`gma.shapes.rectangle` >> :api:`gma.moveable` >> :api:`gma.enemy`
    =================== ========================================================================




Tags
----


*shape*, *moveable*, *enemy*, *rebound*, *deathtouch*, *weakhead*, *patrolling*





Properties
----------


.. admonition:: Inherited from :api:`gma.moveable`

	:prop:`yState <gma.moveable.yState>`, :prop:`xState <gma.moveable.xState>`, :prop:`lastXState <gma.moveable.lastXState>`, :prop:`velocity <gma.moveable.velocity>`, :prop:`jumpVelocity <gma.moveable.jumpVelocity>`

.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:prop:`points <gma.shapes.rectangle.points>`, :prop:`edges <gma.shapes.rectangle.edges>`, :prop:`width <gma.shapes.rectangle.width>`, :prop:`height <gma.shapes.rectangle.height>`, :prop:`depth <gma.shapes.rectangle.depth>`, :prop:`z <gma.shapes.rectangle.z>`, :prop:`x <gma.shapes.rectangle.x>`, :prop:`y <gma.shapes.rectangle.y>`, :prop:`centre <gma.shapes.rectangle.centre>`, :prop:`left <gma.shapes.rectangle.left>`, :prop:`right <gma.shapes.rectangle.right>`, :prop:`top <gma.shapes.rectangle.top>`, :prop:`bottom <gma.shapes.rectangle.bottom>`, :prop:`yOffset <gma.shapes.rectangle.yOffset>`, :prop:`xOffset <gma.shapes.rectangle.xOffset>`, :prop:`type <gma.shapes.rectangle.type>`, :prop:`alive <gma.shapes.rectangle.alive>`, :prop:`solid <gma.shapes.rectangle.solid>`, :prop:`tags <gma.shapes.rectangle.tags>`






Methods
-------


.. admonition:: Inherited from :api:`gma.enemy`

	:metho:`getMovement <gma.enemy.getMovement>`, :metho:`determineState <gma.enemy.determineState>`, :metho:`collided <gma.enemy.collided>`, :metho:`behaviour__jumping <gma.enemy.behaviour__jumping>`, :metho:`behaviour__platformer <gma.enemy.behaviour__platformer>`, :metho:`behaviour__patrolling <gma.enemy.behaviour__patrolling>`, :metho:`collided__rebound <gma.enemy.collided__rebound>`, :metho:`collided__weakhead <gma.enemy.collided__weakhead>`

.. admonition:: Inherited from :api:`gma.moveable`

	:metho:`animate <gma.moveable.animate>`, :metho:`findGround <gma.moveable.findGround>`, :metho:`updatePositions <gma.moveable.updatePositions>`, :metho:`getRotation <gma.moveable.getRotation>`, :metho:`kill <gma.moveable.kill>`

.. admonition:: Inherited from :api:`gma.shapes.rectangle`

	:metho:`setPointsAndEdges <gma.shapes.rectangle.setPointsAndEdges>`, :metho:`setCentre <gma.shapes.rectangle.setCentre>`, :metho:`setBottomLeft <gma.shapes.rectangle.setBottomLeft>`, :metho:`xOf <gma.shapes.rectangle.xOf>`, :metho:`yOf <gma.shapes.rectangle.yOf>`, :metho:`toString <gma.shapes.rectangle.toString>`, :metho:`collided__deathtouch <gma.shapes.rectangle.collided__deathtouch>`




