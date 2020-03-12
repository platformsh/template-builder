require('dotenv').config()

var args = process.argv.slice(2);
console.log(`${process.env[args[0]]}`)
