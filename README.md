# site_info plugin
~A very simple CTFd plugin with the purpose of routing & serving robots.txt through the web app itself.~ My sorry panicked attempt at making robots.txt available on CTFd. Didn't work and not sure why, but can't make the repo private because it's a fork, so enjoy

## Upload to Box

To upload to remote CTFd server running on Ubuntu EC2, use `scp`:

```bash
scp -i /path/to/pem.pem ctfd_site_info_plugin ubuntu@[CTFd_IP]:/home/ubuntu/CTFd/CTFd/plugins/challenges
```
