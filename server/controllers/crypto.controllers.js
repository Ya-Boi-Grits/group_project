const CryptoStrategy = require('../models/crypto.models');

module.exports.findAllCryptoStrategys = (req,res) => {

    CryptoStrategy.find().then((allCryptoStrategys) => {
        res.json({ CryptoStrategys: allCryptoStrategys})
    }).catch((err) => {
        res.status(400).json({ message:"Something went horribly wrong", error: err});
    });

}

module.exports.findOneCryptoStrategy = (req,res) => {
    CryptoStrategy.findOne({_id:req.params.id}).then((oneCryptoStrategy => res.json({ CryptoStrategy: oneCryptoStrategy}))).catch( err => {res.status(400).json({ message:"Something went horribly wrong", error: err});}
    );
}

module.exports.createCryptoStrategy = (req,res) => {
    CryptoStrategy.create(req.body).then(newCryptoStrategy => {
        res.json( { CryptoStrategy: newCryptoStrategy})
    }).catch((err) => {
        res.status(400).json({ message:"Something went horribly wrong", error: err});
    });
}

module.exports.updateCryptoStrategy = (req,res) => {
    CryptoStrategy.findOneAndUpdate({_id:req.params.id}, req.body, { new:true, runValidators:true}).then( updatedCryptoStrategy => {
        res.json( { CryptoStrategy: updatedCryptoStrategy})
    }).catch( err => {
        res.status(400).json({ message:"Something went horribly wrong", error: err});
    });
}

module.exports.deleteCryptoStrategy = (req,res) => {
    CryptoStrategy.findOneAndDelete({_id:req.params.id}).then( result => {
        res.json( {result : result} )}).catch( err => {
            res.status(400).json({ message:"Something went horribly wrong", error: err});
        });
};