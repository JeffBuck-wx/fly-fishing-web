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

const port = 3000;
app.listen(port, () => {
    console.log('App running on port 3000.')
});