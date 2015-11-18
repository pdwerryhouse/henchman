
Example of use:

```python

#!/usr/bin/python

from henchman import File, FILE
from henchman import Package, PACKAGE
from henchman import Host, HOST
from henchman import User, USER
from henchman import Service, SERVICE
from henchman import Group, GROUP
from henchman import Henchman, rules

File("/tmp/baz",
    ensure = "absent",
    contents = "Baz",
    require = FILE("/tmp/blat")
)

File("/tmp/bar",
    ensure = "file",
    contents = "Bar",
    owner = 4000,
    require = USER("zzz")
)

File("/tmp/blat",
    ensure = "absent",
    require = FILE("/tmp/bar")
)

Service("neard",
    enable = "false",
    require = PACKAGE("neard")
)

Package("neard",
    ensure = "present",
)

Service("bluetooth",
    enable = "false",
    require = PACKAGE("bluez")
)

Package("bluez",
    ensure = "present",
)

Package("zsh",
    ensure = "present",
    require = FILE("/tmp/blat")
)

Group("zzz",
    ensure = "present",
    gid = 4000
)

User("zzz",
    ensure = "present",
    comment = "ZZZ ZZZ ZZZ",
    uid = 4000,
    gid = 4000,
    shell = "/bin/zsh",
    home = "/tmp",
    require = GROUP('zzz')
)

Host("blart.home",
    ip="10.1.8.10"
)

Host("snork.home",
    ip="10.1.8.130"
)

rules.run()
```
