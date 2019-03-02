#### arp

- address resolution display and control

example:

```
> arp -a 
? (10.0.1.1) at 78:ca:39:xx:xx:xx on en0 ifscope [ethernet]
? (10.0.1.4) at 84:38:35:xx:xx:xx on en0 ifscope permanent [ethernet]
? (10.0.1.7) at b8:27:eb:xx:xx:xx on en0 ifscope [ethernet]
? (10.0.1.13) at c8:69:cd:xx:xx:xx on en0 ifscope [ethernet]
? (10.0.1.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:xx:xx:xx on en0 ifscope permanent [ethernet]
broadcasthost (255.255.255.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
>
```

10.0.1.7 is the Pi, notice ``b8:27:eb``.
Mac address lookup gives "RASPBERRY PI FOUNDATION .."
