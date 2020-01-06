<!DOCTYPE html>
<?php
  header('Access-Control-Allow-Origin: *');
?>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
    <div>
            <input id="tweet" name="tweet" />
        <button class="btn-header2" onclick="showcode()">sentimen<i
            class="fa"></i></button>
            <div class="" >
				<p id=""> sentimen :  </p>
                <p id="sentimen"> </p>
            </div>
      </div>
	  <script>
		function showcode() {

			var target = document.getElementById("tweet").value;
			var res = {'data':[target]}
			console.log(JSON.stringify(res))
			var xmlHttp = new XMLHttpRequest();
			xmlHttp.open( 'POST', 'http://127.0.0.1:8181/example', false ); // false for synchronous request
			xmlHttp.setRequestHeader('Content-type', 'application/json', 'Access-Control-Allow-Origin: *');
			xmlHttp.send(JSON.stringify(res));
			// xmlHttp.setRequestHeader('Content-type', 'application/json')
			//xmlHttp.send();
			var response = JSON.parse(xmlHttp.responseText);
			var res = response.data[0].sentimen;
			console.log(response.data[0].sentimen)
			document.getElementById("sentimen").innerHTML = res;
		}


		</script>
</body>


</html>