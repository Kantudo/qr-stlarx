# qr-stlarx
Simple qr code generator. Check it out at [qr.stlarx.com](https://qr.stlarx.com)

## Configurations
MUST configure $REPO_DIR/qr_stlarx/qr_stlarx/keys.py. It should look like this.

``` python
SECRET_KEY = 'yourdjangosecretkey'

RECAPTCHA_PUBLIC_KEY = 'recaptchav3publickey' 
RECAPTCHA_PRIVATE_KEY = 'recaptchav3privkey'
```

Originally served using NGINX. Configuration files for uwsgi(interface for communicating nginx with pythom) are located in `` `qr_stlarx/qr-stlarx_uwsgi.ini`` ` and `` `qr_stlarx/uwsgi_params`` `. 
