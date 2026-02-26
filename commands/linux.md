>[!WARNING]
>HOW TO NOT!

### Start Apache & mySQL

>cd /

>cd /opt/lampp

>sudo ./xampp startapache

>sudo ./xampp startmysql

>[!TIP]
>IF! SQL does not start, do `sudo lsof -i :3306` and check for running proccess under 3306
### Example
| COMMAND | PID | USER | FD | TYPE | DEVICE | SIZE/OFF | NODE | NAME |
| ------- | --- | ---- | -- | ---- | ------ | -------- | ---- | ---- |
| mariadbd | 185176 | mysql | 33u | IPv4 | 722971 | 0t0 | TCP | localhost:mysql (LISTEN) |
>[!NOTE]
>MariaDB is running

>sudo systemctl stop mariadb

>sudo ./xampp startmysql
