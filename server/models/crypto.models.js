const mongoose = require('mongoose');

const CryptoStrategySchema = new mongoose.Schema(
    {
        cryptoName: {
            type:String,
            required:[
                true,
                'Coin name is required!'
            ]},
        indicatorName1: {
            type:String,
            required:[
                true,
                'Indicator name is required!'
            ]},
        indicator1: {
            type: Number,
            required :[
                true,
                'Indicator Value is required'
            ]
        },
        indicatorName2: {
            type:String,
            required:[
                true,
                'Indicator name is required!'
        ]
        },
        indicator2: {
            type: Number,
            required :[
                true,
                'Indicator Value is required'
            ]
        }
    }
);

const CryptoStrategy = mongoose.model('CryptoStrategys', CryptoStrategySchema);

module.exports = CryptoStrategy;