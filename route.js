// function route(req, res) {
//   if (req.url === "/") {
//     res.setHeader("content-Type", "text/html");
//     res.write(
//       '<html><form action="/twxt" method="post"><button type="submit">clck</button></form></html>'
//     );
//     return res.end();
//   }
//   if (req.url === "/twxt" && req.method === "POST") {
//     res.statusCode = 302;
//     res.setHeader("Location", "/");
//     return res.end();
//   }
//   console.log(req.url, req.headers);
//   res.setHeader("content-Type", "text/html");
//   res.end();
// }
