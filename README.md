# Tesla-Data
 
 Simple visulization of number of salse Tesla made since 2015 till June 2021.
 

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/jquery.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/jquery-ui.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/ResizeSensor.js"></script>

            <link rel="stylesheet"  href="https://assets.pyecharts.org/assets/jquery-ui.css">

</head>
<body>
    <style>.box {  }; </style>
        <button onclick="downloadCfg()">Save Config</button>
    <div class="box">
                <div id="a4a32a9dcf33494ebe4a451c4b260c0d" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_a4a32a9dcf33494ebe4a451c4b260c0d = echarts.init(
            document.getElementById('a4a32a9dcf33494ebe4a451c4b260c0d'), 'white', {renderer: 'canvas'});
        var option_a4a32a9dcf33494ebe4a451c4b260c0d = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "Model S",
            "legendHoverLink": true,
            "data": [
                0.0,
                2000.0,
                1200.0,
                1700.0,
                1700.0,
                1700.0,
                1700.0,
                1700.0,
                1700.0,
                1700.0,
                1700.0,
                1845.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                1600.0,
                1800.0,
                1800.0,
                2400.0,
                2400.0,
                2400.0,
                2400.0,
                2400.0,
                2400.0,
                2400.0,
                2400.0,
                2400.0,
                2800.0,
                2800.0,
                2800.0,
                1250.0,
                2800.0,
                2800.0,
                1100.0,
                2500.0,
                3750.0,
                1350.0,
                2750.0,
                3250.0,
                875.0,
                800.0,
                2275.0,
                825.0,
                1025.0,
                1750.0,
                975.0,
                1050.0,
                1100.0,
                1235.0,
                1280.0,
                1235.0,
                1900.0,
                1700.0,
                1000.0,
                576.0,
                1280.0,
                1344.0,
                2630.0,
                2338.0,
                2532.0,
                1687.0,
                1386.0,
                1928.0,
                1330.0,
                1330.0,
                1496.0,
                338.0,
                325.0,
                338.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "50%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        },
        {
            "type": "bar",
            "name": "Model X",
            "legendHoverLink": true,
            "data": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                30.0,
                12.0,
                55.0,
                75.0,
                150.0,
                250.0,
                250.0,
                250.0,
                250.0,
                250.0,
                250.0,
                250.0,
                250.0,
                250.0,
                250.0,
                1200.0,
                1200.0,
                1200.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2000.0,
                2200.0,
                2200.0,
                2200.0,
                1025.0,
                2200.0,
                2200.0,
                1325.0,
                1400.0,
                3975.0,
                1225.0,
                3200.0,
                4100.0,
                950.0,
                1100.0,
                2175.0,
                1050.0,
                1375.0,
                2725.0,
                1225.0,
                1825.0,
                1675.0,
                1811.0,
                1878.0,
                1811.0,
                1450.0,
                1250.0,
                1000.0,
                648.0,
                1440.0,
                1512.0,
                2735.0,
                2431.0,
                2634.0,
                3711.0,
                3048.0,
                4241.0,
                1634.0,
                1634.0,
                1838.0,
                371.0,
                357.0,
                371.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "50%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        },
        {
            "type": "bar",
            "name": "Model 3",
            "legendHoverLink": true,
            "data": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                117.0,
                145.0,
                345.0,
                1060.0,
                1875.0,
                2485.0,
                3820.0,
                3875.0,
                6250.0,
                6062.0,
                14250.0,
                17800.0,
                22250.0,
                17750.0,
                18650.0,
                25250.0,
                6500.0,
                5750.0,
                10175.0,
                10050.0,
                13950.0,
                20550.0,
                13450.0,
                13150.0,
                20250.0,
                15566.0,
                16143.0,
                15566.0,
                19000.0,
                17500.0,
                8000.0,
                5400.0,
                12000.0,
                12600.0,
                31208.0,
                27740.0,
                30052.0,
                14506.0,
                11916.0,
                16578.0,
                7395.0,
                7395.0,
                8320.0,
                9590.0,
                9221.0,
                9590.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "50%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                "Model S",
                "Model X",
                "Model 3"
            ],
            "selected": {
                "Model S": true,
                "Model X": true,
                "Model 3": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "Jan 2015",
                "Feb 2015",
                "Mar 2015",
                "Apr 2015",
                "May 2015",
                "Jun 2015",
                "Jul 2015",
                "Aug 2015",
                "Sep 2015",
                "Oct 2015",
                "Nov 2015",
                "Dec 2015",
                "Jan 2016",
                "Feb 2016",
                "Mar 2016",
                "Apr 2016",
                "May 2016",
                "Jun 2016",
                "Jul 2016",
                "Aug 2016",
                "Sep 2016",
                "Oct 2016",
                "Nov 2016",
                "Dec 2016",
                "Jan 2017",
                "Feb 2017",
                "Mar 2017",
                "Apr 2017",
                "May 2017",
                "Jun 2017",
                "Jul 2017",
                "Aug 2017",
                "Sep 2017",
                "Oct 2017",
                "Nov 2017",
                "Dec 2017",
                "Jan 2018",
                "Feb 2018",
                "Mar 2018",
                "Apr 2018",
                "May 2018",
                "Jun 2018",
                "Jul 2018",
                "Aug 2018",
                "Sep 2018",
                "Oct 2018",
                "Nov 2018",
                "Dec 2018",
                "Jan 2019",
                "Feb 2019",
                "Mar 2019",
                "Apr 2019",
                "May 2019",
                "Jun 2019",
                "Jul 2019",
                "Aug 2019",
                "Sep 2019",
                "Oct 2019",
                "Nov 2019",
                "Dec 2019",
                "Jan 2020",
                "Feb 2020",
                "Mar 2020",
                "Apr 2020",
                "May 2020",
                "Jun 2020",
                "Jul 2020",
                "Aug 2020",
                "Sep 2020",
                "Oct 2020",
                "Nov 2020",
                "Dec 2020",
                "Jan 2021",
                "Feb 2021",
                "Mar 2021",
                "Apr 2021",
                "May 2021",
                "Jun 2021",
                "Jul 2021",
                "Aug 2021",
                "Sep 2021",
                "Oct 2021",
                "Nov 2021",
                "Dec 2021"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "Number of Sales per Month",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "dataZoom": [
        {
            "show": true,
            "type": "slider",
            "realtime": true,
            "start": 20,
            "end": 80,
            "orient": "horizontal",
            "zoomLock": false,
            "filterMode": "filter"
        }
    ]
};
        chart_a4a32a9dcf33494ebe4a451c4b260c0d.setOption(option_a4a32a9dcf33494ebe4a451c4b260c0d);
    </script>
<br/>                <div id="5ff4fc03b54845b8923f4e7514b86a70" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_5ff4fc03b54845b8923f4e7514b86a70 = echarts.init(
            document.getElementById('5ff4fc03b54845b8923f4e7514b86a70'), 'white', {renderer: 'canvas'});
        var option_5ff4fc03b54845b8923f4e7514b86a70 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "Model S",
                    "value": 139278.0
                },
                {
                    "name": "Model X",
                    "value": 103577.0
                },
                {
                    "name": "Model 3",
                    "value": 561095.0
                }
            ],
            "radius": [
                "30%",
                "75%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "roseType": "area",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "Model S",
                "Model X",
                "Model 3"
            ],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "Number of Sales",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_5ff4fc03b54845b8923f4e7514b86a70.setOption(option_5ff4fc03b54845b8923f4e7514b86a70);
    </script>
<br/>    </div>
    <script>
            $('#a4a32a9dcf33494ebe4a451c4b260c0d').resizable().draggable().css('border-style', 'dashed').css('border-width', '1px');$("#a4a32a9dcf33494ebe4a451c4b260c0d>div:nth-child(1)").width("100%").height("100%");
            new ResizeSensor(jQuery('#a4a32a9dcf33494ebe4a451c4b260c0d'), function() { chart_a4a32a9dcf33494ebe4a451c4b260c0d.resize()});
            $('#5ff4fc03b54845b8923f4e7514b86a70').resizable().draggable().css('border-style', 'dashed').css('border-width', '1px');$("#5ff4fc03b54845b8923f4e7514b86a70>div:nth-child(1)").width("100%").height("100%");
            new ResizeSensor(jQuery('#5ff4fc03b54845b8923f4e7514b86a70'), function() { chart_5ff4fc03b54845b8923f4e7514b86a70.resize()});
            var charts_id = ['a4a32a9dcf33494ebe4a451c4b260c0d','5ff4fc03b54845b8923f4e7514b86a70'];
function downloadCfg () {
    const fileName = 'chart_config.json'
    let downLink = document.createElement('a')
    downLink.download = fileName

    let result = []
    for(let i=0; i<charts_id.length; i++) {
        chart = $('#'+charts_id[i])
        result.push({
            cid: charts_id[i],
            width: chart.css("width"),
            height: chart.css("height"),
            top: chart.offset().top + "px",
            left: chart.offset().left + "px"
        })
    }

    let blob = new Blob([JSON.stringify(result)])
    downLink.href = URL.createObjectURL(blob)
    document.body.appendChild(downLink)
    downLink.click()
    document.body.removeChild(downLink)
}
    </script>
</body>
</html>

 
 
 All data is from https://www.goodcarbadcar.net/
