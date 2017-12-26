window.onload = function() {
    getMap()
};

function getMap(){
    var arr_return = []
    $.get("result", function(data, status){
        arrayOfLines = data.split("\n");
        arrayOfLines.forEach(function(element) {
             line_splitted = element.split('\t')
             if (line_splitted.length == 2){
                     arr_return.push({"id": "US-"+line_splitted[0],"value": parseInt(line_splitted[1])})
                }         
            });
        return AmCharts.makeChart( "chartdiv",{
                                    "type": "map",
                                    "theme": "light",
                                    "colorSteps": 10,
                                    "dataProvider": {"map": "usaLow","areas":arr_return},
                                    "areasSettings": {"autoZoom": true },
                                    "valueLegend": {
                                        "right": 200,
                                        "minValue": "SAD",
                                        "maxValue": "HAPPY"
                                    },
                                    "export": {"enabled": true }
                                }
                            ); 
    });
}