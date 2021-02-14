var mysql = require('mariadb');
require('dotenv').config();

console.log('process.env.DB_HOST=' + process.env.DB_HOST)
console.log('process.env.DB_USER=' + process.env.DB_USER)
console.log('process.env.DB_PASS=' + process.env.DB_PASS)
console.log('process.env.DB_NAME=' + process.env.DB_NAME)

var con = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS
});

/*
con.connect(function(err) {
  if (err) throw err;
  var sql = "CREATE USER IF NOT EXISTS 'fly-fishing'@'%' IDENTIFIED BY 'Canfield=Creek@5wt";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log(result.affectedRows + " record(s) updated");
  });

  sql = "GRANT INSERT,UPDATE,SELECT PRIVILEGES ON '" + process.env.DB_FLYFISHING + "'.* TO 'fly-fisher'@'%';";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log(result.affectedRows + " record(s) updated");
  }); 
});
*/
