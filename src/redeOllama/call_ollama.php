<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ollama prompt</title>
    <link href="css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <?php
    $target_dir = "/uploads";
    if(!is_dir($target_dir)){

      if (!mkdir($target_dir, 0777, true)) {
        die('Failed to create directories...');
      }
    }

    for($i=0; $i<sizeof($_FILES["prompt"]["name"]); $i++){
      chmod($target_dir, 0777);
      foreach ($_FILES["prompt"]["error"] as $key => $error) {
        if ($error == UPLOAD_ERR_OK) {
            $tmp_name = $_FILES["prompt"]["tmp_name"][$key];
            $name = basename($_FILES["prompt"]["name"][$key]);
            move_uploaded_file($tmp_name, "$target_dir/$name");
        }
      }
    }
    
    $prompts=scandir($target_dir);
    for($i=0; $i<sizeof($prompts); $i++){
      if($prompts[$i]!='.' && $prompts[$i]!='..'){

        $ollama_url = "http://localhost:11434/api/generate";
        $prompt_filename="$target_dir/$prompts[$i]";
        $prompt = fopen($prompt_filename, 'r');
        $prompt = fread($prompt, filesize($prompt_filename));
        $model = $_POST["model"];
        $format=json_decode('{"type":"array","items":{"type":"object","properties":{"Comune":{"type":"string"},"Indirizzo":{"type":"string"},"Vani":{"type":"number"},"Locali":{"type":"integer"},"Mq":{"type":"number"},"Bagni":{"type":"integer"},"Piano":{"type":"string"},"Posti auto":{"type":"string"},"N° Procedura":{"type":"string"},"Lotto":{"type":"string"}},"required":["Comune","Indirizzo","Vani","Locali","Mq","Bagni","Piano","Posti auto","N° Procedura","Lotto"]}}');
        $data = [ 'prompt' => $prompt, 'model' => $model, 'stream' => false, 'format' =>  $format];

        $ch = curl_init($ollama_url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        $response = curl_exec($ch);
        $return = json_decode($response, true);
        $dir = './responses';
        if(!is_dir($dir)){
          if (!mkdir($dir, 0777, true)) {
            die('Failed to create directories...');
          }
        }
        
        echo "<p><b>Prompt:</b><br />";
        echo $prompt_filename."<br /><br />";
        if(array_key_exists('response', $return)){
          echo "<b>Risposta:</b><br />".$return['response']."<br /><br />";
          $file=pathinfo($prompt_filename);
          $filename=$file['filename'].'.json';
          $file=fopen('./responses/'.$filename, 'w');
          fwrite($file, $return['response']);
          $url="http://localhost/rede_ollama/responses/$filename";
          file_put_contents($filename, file_get_contents($url));

        }
        else{
          echo "<b>Errore:</b><br />".$return['error']."<br /><br />";
        }
        unlink("$target_dir/$prompts[$i]");
      } 
    }

    ?>
</body>
</html>