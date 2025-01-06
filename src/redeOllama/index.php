<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ollama prompt</title>
    <link href="css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <main>
    <div>
            <div class="container">
                <h4 class="display-4">Prompt per Ollama AI</h4>
                <form method="POST" action="call_ollama.php" enctype="multipart/form-data">
                    <div class="form-group">
                        <label for="model">Model</label>
                        <input class="form-control" type="text" name="model" id="model" placeholder="Inserire model" required />
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