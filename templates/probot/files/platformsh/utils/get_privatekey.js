const fs = require('fs');
require('dotenv').config()

fs.writeFileSync('registration/temp-key.txt', process.env.PRIVATE_KEY, function (err) {
  if (err) throw err;
});
