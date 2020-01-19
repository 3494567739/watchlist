var data = [20];
var time = [];

function addData(shift) {
	if (data[data.length-1]>10 && data[data.length-1]<40){
    data.push((Math.random() - 0.5) + data[data.length - 1]);
	}
	else{
		data.push(data[data.length-2]);
	}
	
    if (shift){ 
        data.shift();
		}
}

//添加初始数据
for (var i = 1; i < 120; i++) {
    addData();
}
//生成x轴轴标数据
for (var j = 120; j >= 0 ; j--) {
    time.push(j+'秒前')
}

setInterval(function () {
    addData(true);
    myChart.setOption({
		title: {
			text: '温室光照度'
		},
		legend: {
		     data:['光照度（klux）']
		},
        xAxis: {
            data: time
        },
    	yAxis: {
        	boundaryGap: [0, '20%'],
        	type: 'value'
    	},
        series: [{
            name:'光照度（klux）',
			type:'line',
            //smooth:true,
            symbol: 'none',
            stack: 'a',
            areaStyle: {
                normal: {}
            },
            data: data
        }]
    });
}, 1000);