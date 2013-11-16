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
