const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io"); 
const io = new Server(server);

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/mindful_messaging.html");
});

io.on("connection", () => {
  console.log("a user connected");
	console.on("disconnect", () => {
		console.log("user disconnected");
	});
});
	
server.listen(3650, () => {
  console.log("listening on port 3650");
});
