<VirtualHost *:80>
    ServerName ${configuration:www-domain}

    Redirect permanent / https://${configuration:www-domain}/

</VirtualHost>

<VirtualHost *:443>
    ServerAdmin ${configuration:server-admin}
    ServerName ${configuration:www-domain}
    ServerAlias ${configuration:www-domain}

    RewriteEngine On

    RewriteRule ^/(.*) http://localhost:${configuration:pound-port}/VirtualHostBase/https/${configuration:www-domain}:443/${configuration:plone-site}/VirtualHostRoot/$1 [P,L]
    Include ${configuration:custom-vh-config}

    SSLEngine on
    SSLCertificateFile /etc/pki/tls/certs/eea-rapidssl-starcert.pem
    SSLCertificateKeyFile /etc/pki/tls/private/eea-rapidssl-starcert-nopwd.key
    SSLCertificateChainFile /etc/pki/tls/certs/eea-rapidssl-starcert-intermediateCA.pem

    RewriteCond %{REQUEST_METHOD} ^(PUT|DELETE|PROPFIND|OPTIONS|TRACE|PROPFIND|PROPPATCH|MKCOL|COPY|MOVE|LOCK|UNLOCK)$
    RewriteRule .* - [F,L]

</VirtualHost>