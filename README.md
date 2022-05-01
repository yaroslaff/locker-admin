# locker-admin

## Generate self-signed SSL cert onliner
openssl req -subj '/CN=localhost'  -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout localhost.key -out localhost.crt