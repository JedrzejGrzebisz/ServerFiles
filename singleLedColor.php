<?php

$ledDisplay = array();
$ledDisplayFile = fopen("singleLedColor.json", w);

$ledDisplay['row'] = (int)($_POST['row']);
$ledDisplay['column'] = (int)($_POST['column']);
$ledDisplay['color'] = $_POST['color'];

$ledDisplayJson = json_encode($ledDisplay);
fwrite($ledDisplayFile, $ledDisplayJson);
fclose($ledDisplayFile);

exec('sudo ./singleLedColor.py');

?>