<?php

declare(strict_types=1);

use App\Messages;

require __DIR__.'/../vendor/autoload.php';
?>
<html>
<head>
    <title>Platform.sh PHP service examples</title>
    <style type="text/css">
        details {
            margin-top: 1em;
            border: 1px solid #aaa;
            border-radius: 4px;
            padding: 0.5em;
            wdith: 90%;
        }

        summary {
            font-weight: bold;
            margin: -.5em -.5em 0;
            padding: .5em;
        }

        details[open] {
            padding: .5em;
        }

        details[open] summary {
            border-bottom: 1px solid #aaa;
            margin-bottom: .5em;
        }

        table, table td, table th {
            border: 1px solid black;
        }

    </style>
</head>
<body>

<h1>Service examples for PHP</h1>

<?php

function capture_output(callable $callable) {
    ob_start();
    $callable();
    $contents = ob_get_contents();
    ob_end_clean();
    return $contents;
}

$files = glob("../examples/*.php");
foreach ($files as $filename) {
    $name = pathinfo($filename)['filename'];
    $source = highlight_file($filename, true);
    $output = capture_output(function() use ($filename) {
        include $filename;
    });

    print <<<END
<details>
<summary>{$name} Sample Code</summary>    
<section>
<h3>Source</h3>
{$source}
</section>
<section>
<h3>Output</h3>
{$output}
</section>
</details>
END;
}
?>

</body>
</html>
