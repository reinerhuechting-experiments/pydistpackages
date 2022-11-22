#%%
from package1.module1 import foo as foo11

#%%
foo11()

#%%
import package1.module2

# %%
package1.module2.foo()

# %%
import package2.module1

# %%
package2.module1.foo()
# %%

#%%
import nopackage.module1

#%%
nopackage.module1.foo()
#%%
from package1.subpackage import submodule1

#%%
submodule1.foo()

# %%
import nopackage.subpackage.submodule1
# %%
nopackage.subpackage.submodule1.foo()
# %%
import package2.module2
#%%
package2.module2.bar()
# %%
import nopackage.module2

# %%
nopackage.module2.bar()

# %%
