<?php
  $prompt_dir = './uploads';
  $response_dir = './responses';
  $download = false;

  if(!is_dir($prompt_dir)){
    if (!mkdir($prompt_dir, 0777, true)) {
      die('Failed to create directories...');
    }
  }

  if(!is_dir($response_dir)){
    if (!mkdir($response_dir, 0777, true)) {
      die('Failed to create directories...');
    }
  }

  foreach (scandir($prompt_dir) as $file) {
    if ($file !== '.' && $file !== '..') {
      unlink($prompt_dir.'/' . $file);
    }
  }

  foreach (scandir($response_dir) as $file) {
    if ($file !== '.' && $file !== '..') {
      unlink($response_dir.'/' . $file);
    }
  }

  for($i=0; $i<sizeof($_FILES["prompt"]["name"]); $i++){
    chmod($prompt_dir, 0777);
    foreach ($_FILES["prompt"]["error"] as $key => $error) {
    if ($error == UPLOAD_ERR_OK) {
      $tmp_name = $_FILES["prompt"]["tmp_name"][$key];
      $name = basename($_FILES["prompt"]["name"][$key]);
      move_uploaded_file($tmp_name, "$prompt_dir/$name");
      fread(fopen("$prompt_dir/$name", 'r'),filesize("$prompt_dir/$name"));
      }
    }
  }
    
  $prompts=scandir($prompt_dir);
  for($i=0; $i<sizeof($prompts); $i++){
    if($prompts[$i]!='.' && $prompts[$i]!='..'){
      $ollama_url = "http://localhost:11434/api/generate";
      $prompt_filename="$prompt_dir/$prompts[$i]";
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
      if(array_key_exists('response', $return)&&!array_key_exists('error', $return)){
        $file=pathinfo($prompt_filename);
        $filename=$file['filename'].'.json';
        $file=fopen('./responses/'.$filename, 'w');
        fwrite($file, $return['response']);
        $download = true;
      }
      elseif(array_key_exists('error', $return)){
        echo '<p>'.$return['error'].'</br>Modello non disponibile sul server</p>';
        $download = false;
        exit();
      }
    } 
  }

  if(is_dir($response_dir)&& $download){
    $zip = new ZipArchive();
    $zip_file = $response_dir.'/responses.zip';
    if ($zip->open($zip_file, ZipArchive::CREATE) !== TRUE) {
      die('Impossibile creare il file ZIP');
    }

    foreach (scandir($response_dir) as $file) {
      if ($file !== '.' && $file !== '..') {
        $zip->addFile($response_dir.'/' . $file, $file);
      }
    }
    $zip->close();
    header('Content-Type: application/zip');
    header('Content-Disposition: attachment; filename="responses.zip"');
    header('Content-Length: ' . filesize($zip_file));
    readfile($zip_file);
    exit();
    
}

?>