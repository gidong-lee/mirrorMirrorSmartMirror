/* ========================================================================= */
/*  Preloader
/* ========================================================================= */
jQuery(window).load(function() {});
/* ========================================================================= */
/*  Welcome Section Slider
/* ========================================================================= */
$(function() {});
$(document).ready(function() {
    var userList = [{
        'value': "이기동"
    }, {
        'value': "김현정"
    }, {
        'value': "이지원"
    }, {
        'value': "김주영"
    }, {
        'value': "김나래"
    }, {
        'value': "박동조"
    }, {
        'value': "박성욱"
    }, {
        'value': "양중근"
    }];
    $('#userTmpl').tmpl(userList).appendTo("#userListEl");
});


function call_tts(text) {
    $("#talk").text(text);
    var parameters = {
        onstart: startTTSCallback,
        onend: voiceEndCallback
    }
    responsiveVoice.speak(text, "Korean Female", parameters);
}

function startTTSCallback() {
    console.log("startTTS");
    //annyang.pause();
}

function voiceEndCallback() {
    setInterval(function() {
        //annyang.resume();
    }, 2000);
    console.log("endTTS");
}

function showMaker(){
    $("a[href='#MAKER']").trigger("click");
}

function closeYoutube(){
    if($(".fancybox-close")){
        call_tts('동영상 종료');
        $(".fancybox-close").trigger("click");
    }
}

function showYouTubeNum(num){
    var movieNum = 0;
    switch(num){
        case '첫':
        case '1':
            movieNum = 1;break;
        case '두':
        case '2':
            movieNum = 2;break;
        case '세':
        case '3':
            movieNum = 3;break;
        case '네':
        case '4':
            movieNum = 4;break;
        case '다섯':
        case '5':
            movieNum = 5;break;
        case '여섯':
        case '6':
            movieNum = 6;break;
    }
    if(movieNum){
        call_tts(movieNum + '번째 동영상 실행');
        $(("#videoId" + movieNum)).trigger("click");
    }
   
}

function showYouTube(title) {
    var url = "youtube.json";
    
    call_tts(title + ' 동영상 검색');

    $.ajax({
        url: url,
        dataType: 'json',
        data: {
            'text': title
        },
        success: function(data) {
            var items = data.items;
            //$("#youtubeDiv")[0].src = "http://www.youtube.com/embed/"+data.items[0]["id"].videoId+"?autoplay=1&origin=http://127.0.0.1";

            call_tts(data.items.length + '개 동영상이 검색 되었습니다.');

            var youtubeList = [];
            for (var mIdx = 0; mIdx < data.items.length; mIdx++) {
                var tempItem = {};
                var youtubeItem = data.items[mIdx];
                tempItem.index = mIdx + 1;
                tempItem.videoId = youtubeItem.id.videoId;
                tempItem.title = youtubeItem.snippet.title;
                tempItem.imageUrl = youtubeItem.snippet.thumbnails.high.url;

                youtubeList.push(tempItem);
            }
            $("#youtubeListEl").empty();
            $('#youtubeTmpl').tmpl(youtubeList).appendTo("#youtubeListEl");
            $("a[href='#YOUTUBE']").trigger("click");

        }
    });
}

function ledControl(status) {
    var url;
    if (status == true) {
        url = "/ledon.json"
    } else {
        url = "/ledoff.json"
    }
    $.ajax({
        url: url,
        dataType: 'json',
        data: {},
        success: function(data) {
            if (data.txt) {
                call_tts(data.txt);
            }
        }
    });
}

function showLotto() {
    var lotto = new Array(6);
    var count = 0;
    var mFlag = true;
    while (count < 6) {
        var number;
        number = parseInt(Math.random() * 45) + 1
        for (var i = 0; i < count; i++)
            if (lotto[i] == number) mFlag = false;
        if (mFlag) {
            lotto[count] = number;
            count++;
        }
        mFlag = true;
    }
    // 추첨된 로또번호 출력

    var numList = [];

    for (var mIdx = 0; mIdx < lotto.length; mIdx++) {
        numList.push({"value":lotto[mIdx]});
    }
    $("#lottoListEl").empty();
    $('#userTmpl').tmpl(numList).appendTo("#lottoListEl");
    $("a[href='#LOTTO']").trigger("click");
    call_tts('로또 사서 대박나세요');



}

function showTodayWeather(){
    var latitude;
    var longitude;
    
    navigator.geolocation.getCurrentPosition(function(position) {
      latitude = position.coords.latitude;
      longitude = position.coords.longitude;
      
      var url = "/weatherInfo?latitude="+latitude+"&longitude="+longitude;

      $.ajax({
          url: url,
          dataType: 'json',
          data : {
            latitude : latitude,
            longitude : longitude
          },
          success: function(weatherInfo) {
            var tts_text = weatherInfo.grid.city + ' ' + weatherInfo.grid.county + ' 날씨는 ' + weatherInfo.sky.name + '입니다';
            call_tts(tts_text);

            var weatherObj = {};
            weatherObj.code = weatherInfo.sky.code;
            weatherObj.name = weatherInfo.sky.name;
            weatherObj.position = weatherInfo.grid.city + ' ' + weatherInfo.grid.county;
            weatherObj.tc = weatherInfo.temperature.tc;
            weatherObj.tmin = weatherInfo.temperature.tmin;
            weatherObj.tmax = weatherInfo.temperature.tmax;
            weatherObj.humidity = weatherInfo.humidity;
            weatherObj.timeRelease = weatherInfo.timeRelease;

            $("#weatherTimeSpan").parent().show();
            $("#weatherTimeSpan").text(weatherObj.timeRelease);
            $("#weatherPositionSpan").text(weatherObj.position);
            $("#weatherSky").addClass(weatherObj.code);
            $("#weatherSkySpan").text(weatherInfo.sky.name);
            $("#weatherThermometerSpan").text("현재온도 : " + weatherObj.tc + "c");
            $("#weatherHumidifySpan").text(weatherObj.humidity + "%");

            $("a[href='#WEATHER']").trigger("click");


            //$("#weatherText").text(weatherInfo);
          }
      });
    });
}
/*weatherInfo.sky.code
"SKY_O07"
weatherInfo.sky.name
"흐림"
weatherInfo.temperature.tc
"18.90"
weatherInfo.temperature.tmax
"22.00"
weatherInfo.temperature.tmin
"15.00"
*/

window.onload = function() {
    if (annyang) {
        var commandsDefault = {
            '*talk': function(talk) {
                call_tts(talk);
            }
        };
        var commands = {
            '거울아 :userName 보여줘': function(userName) {
                call_tts(userName + ' 일어났습니다.');
            },
            '거울아 :title 동영상 검색': function(title) {
                showYouTube(title);
            },
            ':num번째 동영상 실행': function(num) {
                showYouTubeNum(num);
            },
            '동영상 종료': function() {
                closeYoutube();
            },
            '거울아 만든 사람들 보여 줘': function() {
                showMaker();            
            },
            '거울아 날씨': function() {
                showTodayWeather();
            },
            '거울아 돈벌기': function() {
                showLotto();
            },'야 불 켜': function() {
                //call_tts("야 불 켜");
                ledControl(true);
            },
            '야 불 꺼': function() {
                //call_tts("야 불 꺼");
                ledControl(false);
            }
        };
        //annyang.setLanguage("en-US");
        annyang.setLanguage("ko");
        //annyang.addCommands(commandsDefault);
        annyang.addCommands(commands);
        annyang.debug(true);
        annyang.addCallback('resultNoMatch', function(userSaid) {
            $("#talk").text("not match : " + userSaid);
            console.log("userSaid : " + userSaid); // sample output: 'hello'
        });
        annyang.start({});
    }
}