# Architecture

The matplotlib uses components that it registers as QML-Objects that can then be used as templates.

All components wrap a matplotlib [Artist](https://matplotlib.org/stable/api/artist_api.html) object. It's possible to modify the artist directly by reaching through the wrapper object to get the original matplotlib object. This is not recommended because the wrapper objects keeps the state due to how the initialization in QML works and applies it on the wrapped `Artist`.

The documentation page of a component contains a **Properties** header. This is to be read as follows:

## Structure of this documentation

The documentation lists the functionality of a plugin component and also the component that it inherits from. The inheritance structure is very similar to the one from [matplotlib](https://matplotlib.org/3.3.3/contents.html).

### property-name (property-type)
(This is the name of the property in QML)

(short description about what it does)

**Python Methods**
(A table about the corresponding Python interface. Using these methods is the same as reading or writing to a QML property)

## Numpy values

Numpy objects or data-types aren't supported by QML resulting in unexpected behaviour when the property is read in QML (no errors). because of that all numpy types are converted into native python data types before the getter returns them.