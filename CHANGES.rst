Changes
=======

4.2.0 (2016-12-08)
------------------

- Raise more informative KeyError subclasses from the utility when intids
  or objects cannot be found. This distinguishes them from errors
  raised by normal dictionaries or BTrees, and is useful in unit
  testing or when persisting intids or sharing them among processes
  for later or concurrent use.

- Propagate ``POSKeyError`` from ``queryId`` instead of returning the
  default object. This exception indicates a corrupt database, not a
  missing object. The ``queryObject`` function already behaved this way.

- Stop depending on ZODB for anything except testing.

- Add support for Python 3.5 and PyPy3 5.2.

- Drop support for Python 2.6.

4.1.0 (2014-12-27)
------------------

- Add support for PyPy (PyPy3 blocked on PyPy3-compatible ``zodbpickle``).

- Add support for Python 3.4.


4.0.0 (2014-12-20)
------------------

- Add support for testing on Travis.


4.0.0a1 (2013-02-22)
--------------------

- Add support for Python 3.3.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.

- Bug fix: ensure that the IntId utility never generates ids greater
  than the maxint of the BTree family being used.

3.7.2 (2009-12-27)
------------------

- Use the zope.component API in favor of ztapi.

- Remove ``zope.app.testing`` dependency.

3.7.1 (2009-05-18)
------------------

- Remove dependencies on ``zope.container``.  Instead import
  ``Object*Event`` classes from ``zope.lifecycleevent`` and import
  ``IContained`` from ``zope.location``.  In order to be able to do
  this, depend on ``zope.lifecycleevent``>=3.5.2 and
  ``zope.location``>=3.5.4.

- Remove a dependency on ``zope.container.contained.Contained``
  (this is a dumb base class that defines __parent__ and __name__
  as None and declares that the class implements IContained).

3.7.0 (2009-02-01)
------------------

- Split out this package from ``zope.app.intid``. The latter one
  now only contains browser views and compatibility imports while
  whole IntId functionality is moved here.
