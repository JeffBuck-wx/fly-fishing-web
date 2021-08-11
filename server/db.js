const Pool = require("pg").Pool;

const pool = new Pool({
  user: "fly_fisher",
  password: "WhitewaterNo.5_45",
  host: "localhost",
  port: 5432,
  database: "fly_fishing"
});

module.exports = pool;