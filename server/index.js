const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./db");

//middleware
app.use(cors());
app.use(express.json()); //req.body

//ROUTES//
app.get('/*', (req, res) => {
  res.send("Hello World")
});

app.listen(3001, () => {
  console.log("running on port 3001.")
});

