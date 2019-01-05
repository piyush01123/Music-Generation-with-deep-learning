function doPlay(m, btn) {
    if (btn.value == 'play') {
        m.play();
        btn.value = 'stop';
    }
    else {
        m.stop();
        btn.value = 'play';
    }
};
var mp2;

  $(document).ready(function () {
  var midifile;
  $("#btnfile").click(function () {
  $("#uploaded_midi").click();
});


console.log(doPlay);




  $("#uploaded_midi").change(function () {
    // midifile=$(this).val().replace(/C:\\fakepath\\/ig,'');
    midifile=$(this).val();
  console.log(midifile);
  var temp = midifile.replace(/C:\\fakepath\\/ig,'');
  $("#fname").text("You have uploaded " + temp);
  });

  $("#submitbutton").click(function () {
    console.log('clicked', midifile);
    // $("#results").html('');
    var form = new FormData();
    var fileInputElement = document.getElementById('uploaded_midi');
    // form.append("midifile", midifile);
    form.append("midifile", fileInputElement.files[0]);
    console.log(form);
    $.ajax({
              type: 'POST',
              url: `/generate`,
              processData: false,
              contentType: false,
              async: false,
              cache: false,
              data: form,
              success: function (data) {
                console.log('check'+doPlay);

                // $("#results").html('');
                console.log(data);
                // $("#results").append(data.generated);
                // $("#results").append("<audio controls><source src='" + data.generated + "' type='audio/midi' </audio>");
                // $("#results").append("<audio controls><source src='" + data.generated + "' type='audio/midi' </audio>");
                var stuff = "MIDIjs.play('" + data.generated + "');";
                console.log(stuff);
                // $("#results").append("<a href='#' onClick=" + stuff + ">Play My Song</a>");

                // $("#results").append("<input type='button' value='play' id='btn2' onclick='doPlay(mp2,this);'/>");
                mp2 = new MidiPlayer(data.generated, 'btn2');
                }
          })
  })
})
