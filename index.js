const app = require('express')();
const wsInstance = require('express-ws')(app);

app.ws('/', ws => {
	ws.on('message', data => {
		wsInstance.getWss().clients.forEach(server => {
			if (server !== ws) {
				server.send(data);
			}
		});
	});
});

app.get('/', (req, res) => {
	res.sendFile('./client/index.html', { root: __dirname });
});

app.get('/p2p', (req, res) => {
	res.sendFile('./client/p2p.html', { root: __dirname });
});

app.listen(8080);