===============================================
python-cordova
===============================================

This is a very simple Python library to interface with the Cordova (Phonegap) command line tool.


Key concepts
===============================================
- Interact with the Cordova CLI directly from Python
- Enables building and archiving PhoneGap applications from your Python code


Usage
===============================================

.. code-block:: python
   import cordova

   application = cordova.App(
       'PhoneGap Application',
       APPLICATION_ROOT
   )

   application.build('android') # or any installed platform
   application.archive('ios') # or any installed platform