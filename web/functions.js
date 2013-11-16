function pimp3clock_main() {
  songUpdate(1000);
  
  $("#select").click(function(){
    $.getJSON('select.json',
    {},
    function(data) {
    });
  });
  
  $("#next").click(function(){
    $.getJSON('next.json',
    {},
    function(data) {
      songUpdate(0);
    });
  });
  
  $("#previous").click(function(){
    $.getJSON('previous.json',
    {},
    function(data) {
      songUpdate(0);
    });
  });
  
  $("#update").click(function(){
    $.getJSON('update.json',
    {},
    function(data) {
      songUpdate(0);
    });
  });
  
  $(".b-red").click(function(){
    $.getJSON('background.json',
    {color: 1},
    function(data) {
    });
  });
  
  $(".b-green").click(function(){
    $.getJSON('background.json',
    {color: 2},
    function(data) {
    });
  });
  
  $(".b-blue").click(function(){
    $.getJSON('background.json',
    {color: 4},
    function(data) {
    });
  });
  
  $(".b-yellow").click(function(){
    $.getJSON('background.json',
    {color: 3},
    function(data) {
    });
  });
  
  $(".b-teal").click(function(){
    $.getJSON('background.json',
    {color: 6},
    function(data) {
    });
  });
   
  $(".b-violet").click(function(){
    $.getJSON('background.json',
    {color: 5},
    function(data) {
    });
  });
  
  $(".b-white").click(function(){
    $.getJSON('background.json',
    {color: 7},
    function(data) {
    });
  });
  
  $(".volume").on("slidestop", function( event, ui ){
    $.getJSON('volume.json',
    {vol: $(".volume").val()},
    function(data) {
      songUpdate(0);
    });
  });
}

function songUpdate(interval) {
   $.getJSON('status.json',
   {},
   function(data) {
     $("#artist").html(data.song.artist);
     $("#album").html(data.song.album);
     $("#song").html(data.song.title);
     $("#elapsed").html(data.status.elapsed + " / " + data.song.time);
     $(".volume").val(data.status.volume);
     $(".volume").slider('refresh');
     $(".playpause").removeClass( "play pause stop" ).addClass(data.status.state);
     
   });
   if (interval!=0) {
       window.setTimeout("songUpdate("+interval+")",interval);
   }
}
