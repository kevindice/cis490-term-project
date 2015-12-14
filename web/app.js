var express = require('express');
var app = express();
var mongo = require('mongodb').MongoClient;
var _ = require('lodash');


mongo.connect('mongodb://localhost:27017/test', function(err, db){
    var col = db.collection('ngram');
    app.get('/query', function(req, res){
        var cleaned = req.query.ngram.replace(/\W/g, '');
        col.find({ngram: cleaned}, {sort:'week'}).toArray(function(err, result){
            res.send(result);
        });
    })
});


app.set('view engine', 'jade');

app.use(express.static('static'));
app.use(express.static('.'));

app.get('/', function (req, res) {
  res.render('index');
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
