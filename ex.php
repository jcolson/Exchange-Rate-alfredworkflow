//old - not used any longer
<?php
$key = "9e494a42ebb50cd67a922af6ad6e8369";
$url = "http://data.fixer.io/api/latest?access_key=$key&symbols=USD,EUR,GBP&format=1";
$result = json_decode(CallAPI("GET", $url));
//echo date("m/d/y G:i:s T",$result->timestamp)." - ";
$gbp = round($result->rates->GBP / $result->rates->USD,2);
$eur = round($result->rates->EUR / $result->rates->USD,2);
echo "{\"items\": [";
echo "{\"uid\":\"USD\",";
echo "\"title\":\"USD\",";
echo "\"subtitle\":\"1.00\",";
echo "\"arg\":\"1.00\"}";

echo ",{\"uid\":\"GBP\",";
echo "\"title\":\"GBP\",";
echo "\"subtitle\":\"".$gbp."\",";
echo "\"arg\":\"".$gbp."\"}";

echo ",{\"uid\":\"EUR\",";
echo "\"title\":\"EUR\",";
echo "\"subtitle\":\"".$eur."\",";
echo "\"arg\":\"".$eur."\"}";

echo "]}";

function CallAPI($method, $url, $data = false) {
    $curl = curl_init();

    switch ($method)
    {
        case "POST":
            curl_setopt($curl, CURLOPT_POST, 1);

            if ($data)
                curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
            break;
        case "PUT":
            curl_setopt($curl, CURLOPT_PUT, 1);
            break;
        default:
            if ($data)
                $url = sprintf("%s?%s", $url, http_build_query($data));
    }

    // Optional Authentication:
    //curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
    //curl_setopt($curl, CURLOPT_USERPWD, "username:password");

    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

    $result = curl_exec($curl);

    curl_close($curl);
    //echo $result;
    return $result;
}
?>