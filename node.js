// const http =require("http");

// const rou = require('./route');

// const server =http.createServer(rou);

// server.listen(5000);
const express = require("express");
const app = express();
const port = 3000;

app.get("/get_rfid/:id", (req, res) => {
  console.log("newcard");
  console.log("Requested URL:", req.originalUrl); // Print the URL
  res.json({ status: "done" }); // Send JSON response
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
