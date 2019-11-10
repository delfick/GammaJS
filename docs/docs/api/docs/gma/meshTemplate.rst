

.. api:: gma.meshTemplate


.. api:: meshTemplate



gma.meshTemplate
================


    Provides the specification of an object which is using a mesh



    =================== =========================
    Package             gma/utils/render
    Inheritance chain   :api:`gma.baseTemplate`
    =================== =========================







Properties
----------


.. admonition:: Inherited from :api:`gma.baseTemplate`

	:prop:`sceneHelper <gma.baseTemplate.sceneHelper>`, :prop:`_blueprint <gma.baseTemplate._blueprint>`, :prop:`xRot <gma.baseTemplate.xRot>`, :prop:`yRot <gma.baseTemplate.yRot>`, :prop:`zRot <gma.baseTemplate.zRot>`, :prop:`xScale <gma.baseTemplate.xScale>`, :prop:`yScale <gma.baseTemplate.yScale>`, :prop:`zScale <gma.baseTemplate.zScale>`, :prop:`xOffset <gma.baseTemplate.xOffset>`, :prop:`yOffset <gma.baseTemplate.yOffset>`, :prop:`zOffset <gma.baseTemplate.zOffset>`






Methods
-------


.. admonition:: Inherited from :api:`gma.baseTemplate`

	:metho:`getInstance <gma.baseTemplate.getInstance>`




.. index:: pair: meshTemplate; defineInstance()

.. _gma.meshTemplate.defineInstance:


.. metho:: gma.meshTemplate.defineInstance


**defineInstance** ( ) -> :glge:`Object`
    | Meshtemplate will look for mesh and material options
    | It will create mesh and material objects from these options
    | That are then attached a GLGE Object, which is returned
    

    **Overrides** :metho:`gma.baseTemplate.defineInstance <gma.baseTemplate.defineInstance>`
    







