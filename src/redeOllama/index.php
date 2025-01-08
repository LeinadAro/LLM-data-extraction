<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>redeOllama</title>
    <link href="css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <main>
    <div>
            <div class="container">
                <h4 class="display-4">Estrazione dati di immobili</h4>
                <form method="POST" action="call_ollama.php" enctype="multipart/form-data">
                    <div class="form-group">
                        <label for="model">Model</label>
                        <select class="form-control" name="model" id="model" required>
                            <?php
                                #visualizza modelli disponibili sul server come opzioni del select
                                $ollama_url = "http://localhost:11434/api/tags";                          
                                $ch = curl_init($ollama_url);
                                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
                                $response = curl_exec($ch);
                                $return = json_decode($response, true);
                                if(array_key_exists("models", $return)){
                                    foreach($return["models"] as $key => $value){
                                        echo '<option>'.$value["name"].'</option>';
                                    }
                                }
                                curl_close($ch);
                            ?>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="prompt">Prompt</label>
                        <input class="form-control" type="file" name="prompt[]" id="prompt[]" multiple="multiple" required />
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary">Invia</button>
                    </div>
                </form>
            </div>
        </div>
    </main>
</body>
</html>