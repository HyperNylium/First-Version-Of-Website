function checkPassword()
{
	var password = document.getElementById('passwordBox');
	var passwordText = password.value;
	if(passwordText == "1234") {
		alert("Authentication Successful. Click > Ok < To Proceed");
		window.location.href = ( "  " );

	}

	alert("Authentication Failed, Click > Ok < To Try Again. ");
		return false;
	}
