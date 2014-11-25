<?php
$file = $argv[1];
function characterSplit($string) {
        return str_split($string);
        };

function jHash($string) {
        $hash = false;
        $hash1 = 0;
        $base = base64_encode($string);
        $characters = characterSplit($string);
        foreach ($characters as $character) {
                $hash1 += ord($character);
        };
        /*$hash = $hash1 * strlen($string);*/
        $hash2 = 0;
        $characters = characterSplit($base);
        foreach ($characters as $character) {
                $hash2 += ord($character);
        };
        $hash2 = $hash2 * strlen($base);
        $hash3 = $hash1 | $hash2;
        $hash4 = $string ^ $base;
        $characters = characterSplit($hash4);
        foreach ($characters as $character) {
                $hash4 += ord($character);
        };
        $hash = $hash1 + $hash2 + $hash3 * $hash4;
        return base64_encode($hash);
};

$hashes = 'MzM1MTY0OA== MTE1NjA2Nw== NDIyMDI2MQ== MjQ5NDk2ODA= MTQ4NTg5NzQ= NDM5MDkwNg== NTM4MzQ2MA== Mjg1MjgwNQ== MzA2NTQ4MA== NDIyNDc4MA== Mzc5NzQ3OQ== MzgwMjM3MA== MzEzODg5OQ== MzI4ODkyMA== MTQ2MTgwNA== MTk4MzU3Nzk= NTE1Njc0MA== MzA0NjgxODA= NjUxMzA5OA== MjkyMzQzNjY= MjkyNjM5ODY=';

$handle = fopen($file, "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        // process the line read.
	$line = trim(preg_replace('/\s+/', ' ', $line));
	$hash = jHash($line);
	if (strpos($hashes, $hash) !== false) {
		print "$line $hash\n";
		}
    }
} else {
    // error opening the file.
} 

fclose($handle);
