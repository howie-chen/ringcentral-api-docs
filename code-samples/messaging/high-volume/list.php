<?php
/* You get the environment parameters from your 
   application dashbord in your developer account 
   https://developers.ringcentral.com */
   
require('vendor/autoload.php');
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . '/../');
$dotenv->load();

$SENDER       = $_ENV['SMS_SENDER'];
$RECIPIENT    = $_ENV['SMS_RECIPIENT'];

$rcsdk = new RingCentral\SDK\SDK( $_ENV['RC_CLIENT_ID'],
                                  $_ENV['RC_CLIENT_SECRET'],
                                  $_ENV['RC_SERVER_URL'] );
$platform = $rcsdk->platform();
$platform->login( [ "jwt" => $_ENV['RC_JWT'] ] );

$response = $platform->get('/account/~/extension/~/phone-number');
foreach ($response->json()->records as $record){
	foreach ($record->features as $feature){
		if ($feature == "A2PSmsSender"){
			if ($record->paymentType == "TollFree")
				print_r ($record->phoneNumber." is a toll-free number provisioned for high-volume SMS\n");
			else
				print_r ($record->phoneNumber." is a 10-DLC local number provisioned for high-volume SMS\n");
		}
	}
}
?>