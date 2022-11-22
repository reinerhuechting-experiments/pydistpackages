# This file contains imports and calls to several functions
# in the packages that are defined in this repository.
# This demonstrates how to define and use python packages.

# %%
# Import functions/modules from packages
# package1 and package2
from package1.module1 import foo as foo11
import package1.module2
import package2.module1
import package2.module2

# %% Call the foo() functions from the imported modules.
foo11()
package1.module2.foo()
package2.module1.foo()

# %%
# Import modules from nopackage.
# According to the documentation,
# this is not a valid package

import nopackage.module1
import nopackage.module2

# %%
# Call the foo() functions from the invalid package.
nopackage.module1.foo()
nopackage.module2.foo()
# %%
# Import modules from valid sub packages.
from package1.subpackage import submodule1

# %%
# ... use them.
submodule1.foo()

# %%
# Import modules from invalid sub packages.
import nopackage.subpackage.submodule1

# %%
# ... use them
nopackage.subpackage.submodule1.foo()

# %%
# Use a function that imports something
# from another module in its package.
package2.module2.bar()

# %%
# Same with the invalid package.
nopackage.module2.bar()

# %%
