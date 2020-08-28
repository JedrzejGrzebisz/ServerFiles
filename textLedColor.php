<?php

$ledDisplay = array();
$ledDisplayFile = fopen("textLedColor.json", w);

$ledDisplay['text'] = $_POST['text'];
$ledDisplay['color'] = $_POST['color'];

$ledDisplayJson = json_encode($ledDisplay);
fwrite($ledDisplayFile, $ledDisplayJson);
fclose($ledDisplayFile);

exec('sudo ./textLedColor.py');

?>