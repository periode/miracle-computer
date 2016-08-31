var servi = require('servi');
var app = new servi(true);

port(8080);

serveFiles('public');

route('/', function (req){
	req.serveFile('public/index.html');
});

start();
