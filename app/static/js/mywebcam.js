Webcam.set({
    width: 520,
    height: 240,
    image_format: "jpeg",
    jpeg_quality: 90,
  });
  Webcam.attach("#my_camera");

//   <!-- Code to handle taking the snapshot and displaying it locally -->
  function take_snapshot() {
    // Webcam.reset();

    Webcam.snap(function (data_uri) {
      document.getElementById("result").innerHTML = '<img src="' + data_uri + '"/>';
    });
  }