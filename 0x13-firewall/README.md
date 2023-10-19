# 0x13. Firewall

## <p align="center">![alt text](https://github.com/Dikachis/alx-system_engineering-devops/blob/main/image_devops/Firewall.png?raw=true)</p>

### Resources
**Read or watch:**
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)
- [First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw)
- [How to manage and forward ports with UFW on Ubuntu 18.04](https://www.arubacloud.com/tutorial/how-to-manage-and-forward-ports-with-ufw-on-ubuntu-18-04.aspx)
- [How To Configure Firewall with UFW on Ubuntu 20.04 LTS](https://www.cyberciti.biz/faq/how-to-configure-firewall-with-ufw-on-ubuntu-20-04-lts/)
- [TCP/UDP rules in Firewall - DigitalOcean Tutorials- youTube](https://www.youtube.com/watch?v=Zi-KqDEiBn8)
- [#Setting Up a Basic Firewall](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- [UFW Essentials: Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
- [#Allow MySQL Connection from Specific IP Address or Subnet](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
- [#Adjusting Your Source Server’s Firewall](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [How to configure ufw to forward port 80/443 to internal server hosted on LAN](https://www.cyberciti.biz/faq/how-to-configure-ufw-to-forward-port-80443-to-internal-server-hosted-on-lan/)
- [First 5 Commands When I Connect on a Linux Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)
- [server uptime and downtime](https://www.techtarget.com/whatis/definition/uptime-and-downtime)

## More Info
As explained in the web stack **debugging guide concept** above, ``telnet`` is a very good tool to check if sockets are open with ``telnet IP PORT``. For example, if you want to check if port 22 is open on ``web-02``:
```
