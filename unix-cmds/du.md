du disk usage

The du utility displays the file system block usage

-d depth

-h human readable (

-k Display block counts in 1024-byte (1-Kbyte) blocks.


du  -k | sort -n | tail -n 5

> du  -k | sort -n | tail -n 5
32871636	./Music/iTunes/iTunes Media
33351996	./Music/iTunes
34130948	./Music
59414024	./Video
144002968	.
>