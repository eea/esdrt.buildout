<VirtualHost *:80>
    ServerName ${configuration:www-domain}

    Redirect permanent / https://${configuration:www-domain}/

</VirtualHost>

<VirtualHost *:443>
    ServerAdmin ${configuration:server-admin}
    ServerName ${configuration:www-domain}

    RewriteEngine On

    RewriteRule ^/(.*) http://${haproxy-config:frontend-bind}/VirtualHostBase/https/${configuration:www-domain}:443/Plone/VirtualHostRoot/$1 [P,L]

    SSLEngine on
    SSLCertificateFile /etc/pki/tls/certs/eea-rapidssl-starcert.pem
    SSLCertificateKeyFile /etc/pki/tls/private/eea-rapidssl-starcert-nopwd.key
    SSLCertificateChainFile /etc/pki/tls/certs/eea-rapidssl-starcert-intermediateCA.pem

    RewriteCond %{REQUEST_METHOD} ^(PUT|DELETE|PROPFIND|OPTIONS|TRACE|PROPFIND|PROPPATCH|MKCOL|COPY|MOVE|LOCK|UNLOCK)$
    RewriteRule .* - [F,L]

    <IfModule mod_deflate.c>
        AddOutputFilterByType DEFLATE text/text text/html text/plain text/xml text/css text/javascript application/javascript
    </IfModule>

</VirtualHost>
