<?php
($_=@$_GET['file']) && @substr(file($_)[0], 0, 6) === "@<?php" ? include($_) : highlight_file(__FILE__);
