import c3 from 'c3';
import cs from 'color-scheme';

// Init tags
$("#tags").tagsInput({
    'height': '100px',
    'width': '500',
    'minChars': 1,
    'maxChars': 30,
    'defaultText': 'Add tags here. (Not case sensitive)'
});


var w = $('#viewer').css('width');
var chart = c3.generate({
    width: .5 * parseInt(w.substring(0, w.length - 2)),
    height: 500,
    data: {
        columns: [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 50, 20, 10, 40, 15, 25]
        ]
    },
    bindto: '#chartArea'
});


window.setTimeout(function(){
    chart.resize({height: 600, width: 800})
}, 1000);
