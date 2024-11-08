```bash
ip access-list extended MyACL
 deny ip 10.0.0.0 0.255.255.255 any
 deny ip 172.16.0.0 0.15.255.255 any
 deny ip 192.168.0.0 0.0.255.255 any
 deny ip 127.0.0.0 0.255.255.255 any
 deny ip 224.0.0.0 15.255.255.255 any
 permit tcp host 192.168.0.1 any eq 22
 permit tcp host 192.168.0.15 any eq 22
 permit tcp 192.168.0.0 0.0.0.255 any eq 80
 permit tcp 192.168.0.0 0.0.0.255 any eq 443
 deny ip any any
exit
interface GigabitEthernet0/1
 ip access-group MyACL in
exit

```