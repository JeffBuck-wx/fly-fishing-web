const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./db");

//middleware
app.use(cors());
app.use(express.json()); //req.body

//ROUTES//
app.get("/fish", async (req, res) => {
  try {
    const allFish = await pool.query("SELECT * FROM fish");
    res.json(allFish.rows);
    console.log(allFish.rows);
  } catch (err) {
    console.error(err.message);
  }
});

const port = 3000;
app.listen(port, () => {
    console.log('App running on port 3000.')
});