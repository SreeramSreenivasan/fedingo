// SSL/HTTPS server in NodeJS

var https = require('https');
var fs = require('fs');

var options = {
  key: fs.readFileSync("/path/to/private.key"),
  cert: fs.readFileSync("/path/to/your_domain_name.crt"),
  ca: [
          fs.readFileSync('path/to/CA_root.crt'),
          fs.readFileSync('path/to/ca_bundle_certificate.crt')
       ]
};

https.createServer(options, function (req, res) {
 res.writeHead(200);
 res.end("Hello World");
}).listen(443);

//Run server with following command
//node start server.js
