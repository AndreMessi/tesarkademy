var http = require('http');
var express = require('express');
var app = express();

app.get('/',  function(req,res) {
    res.json(
        [
        { 
        itemId: '12341822',
        itemName: 'desk',
        price: '700000'
    },
        [{
            rating:'akmal',skor:'4',},
            {
                rating:'andi',skor:'5'

            }],
    {
        color:'brown,black'
    }        
    
])

});

app.listen(3000);

console.log('Example app listening on port 3000');