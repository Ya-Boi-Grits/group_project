const CryptoStrategyControllers = require("../controllers/crypto.controllers");

module.exports = app => {
    app.get('/api/cryptostrategy',CryptoStrategyControllers.findAllCryptoStrategys);
    app.get('/api/cryptostrategy/:id',CryptoStrategyControllers.findOneCryptoStrategy);
    app.post('/api/cryptostrategy',CryptoStrategyControllers.createCryptoStrategy);
    app.put('/api/cryptostrategy/:id',CryptoStrategyControllers.updateCryptoStrategy);
    app.delete('/api/cryptostrategy/:id',CryptoStrategyControllers.deleteCryptoStrategy);
};