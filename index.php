<?php
header("Content-Type: application/json");

$nik = $_GET['nik'] ?? '';

$command = "run.py" . escapeshellarg($nik);

echo exec($command, $output, $returnCode);