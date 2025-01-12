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
        <?php 
            $ollama_url = "http://localhost:11434/api/tags";                          
            $ch = curl_init($ollama_url);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
            $response = curl_exec($ch);
            $showExtractionDiv=false;
            $showNoModelDiv=false;
            if(!curl_error($ch)){
                $return = json_decode($response, true);
                if(array_key_exists("models", $return) && count($return["models"])!=0){
                    $showExtractionDiv=true;
                }
                else $showNoModelDiv=true;
                curl_close($ch);
            }
            else echo '<p>Errore: Nessuna connesione a Ollama server</p>';
        ?>
            <div class="container" <?php if($showExtractionDiv==false) echo 'hidden' ?>>
                <h4 class="display-4">Estrazione dati di immobili</h4>
                <form method="POST" action="call_ollama.php" enctype="multipart/form-data">
                    <div class="form-group">
                        <label for="model">Model</label>
                        <select class="form-control" name="model" id="model" required>
                            <?php
                                #visualizza modelli disponibili sul server come opzioni del select
                                if(!curl_error($ch)){
                                    if(array_key_exists("models", $return)){
                                        foreach($return["models"] as $key => $value){
                                            echo '<option>'.$value["name"].'</option>';
                                        }
                                    }
                                }
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
            <div class="container" <?php if($showNoModelDiv==false) echo 'hidden' ?>>
                <h4>Non ci sono modelli disponibili</h4>
                <p>
                    Non sono attualmente disponibili modelli per l'estrazione dati.</br>
                </p>
            </div>
        </div>
    </main>
</body>
</html>