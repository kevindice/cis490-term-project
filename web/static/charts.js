import c3 from 'c3';
import cs from 'color-scheme';
import _ from 'lodash';
import moment from 'moment';

window._ = _;

var ngrams = [];
var regex = /^([A-Z0-9]+\s*)+$/;
var chartDataTitles = {};

var clean = function(ngram){
    return ngram.trim().toUpperCase()
}

var fixUpData = function(data){
    var a =  _.groupBy(data, 'week');
    _.each(a, function(sublist, key){
        a[key] = _.reduce(sublist, function(total, n){
            return total + n.count;
        }, 0);
    });
    return a;
}

var fetch = function(ngram){
    $.ajax({
        method: "GET",
        url: "http://localhost:3000/query?ngram=" + clean(ngram)
    }).then(function(data){
        if(data.length == 0){
            alert("Ngram \"" + clean(ngram)  + "\" Not Found");
            $("#tags").removeTag(ngram);
        } else{
            addToChart(data);
        }
    });
}

var weekToDate = function(week){
    return moment(week * 7 * 24 * 3600 * 1000).format('YYYY-MM-DD');
}

var addToChart = (function(){
    var i = 1;
    return function(data){
        var ng = data[0]['ngram'];
        data = fixUpData(data);
        var x_vals = _(data).keys().map(weekToDate).value();
        var y_vals = _.values(data);
        x_vals.unshift('x' + i);
        y_vals.unshift('data' + i);

        var xs = {};
        xs['data' + i] = 'x' + i;

        names['data' + i] = ng;

        console.log(names);

        chart.load({
            xs: xs,
            columns: [
                x_vals,
                y_vals
            ]
        });

        chartDataTitles[ng] = 'data' + i;
        i++;

        updateNames();
    }
})();

var names = {}
var updateNames = function(){
    chart.data.names(names);
}

var addNgram = function(ngram){
    if(!ngram.match(regex)){
        alert("Invalid phrase.\n\nPhrases should be ALL CAPS and free of punctuation.")
        $("#tags").removeTag(ngram);
        return;
    }

    fetch(ngram);
}

var removeNgram = function(ngram){
    chart.load({
        unload: chartDataTitles[clean(ngram)]
    });
}

// Init tags
$("#tags").tagsInput({
    'height': '100px',
    'width': '500',
    'minChars': 1,
    'maxChars': 30,
    'defaultText': 'Add tags here. (Not case sensitive)',
    'onAddTag': addNgram,
    'onRemoveTag': removeNgram
});









var w = $('#viewer').css('width');
var chart = c3.generate({
    width: .5 * parseInt(w.substring(0, w.length - 2)),
    height: 500,
    data: {
        columns: []
    },
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                culling: { max: 8 },
                format: '%Y-%m-%d'
            }
        }
    },
    bindto: '#chartArea'
});


window.setTimeout(function(){
    chart.resize({height: 600, width: 800})
}, 1000);
