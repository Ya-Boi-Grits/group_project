const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.use(express.urlencoded({extended: true}));

require('./configs/crypto.configs');
require('./routes/crypto.routes')(app);

app.listen(8000, () => {
    console.log("Server up at 8000");
});