<details>
<summary>Drupal: using Lando</summary><br />

Lando supports PHP applications [configured to run on Platform.sh](https://docs.platform.sh/development/local/lando.html), and pulls from the same container registry Platform.sh uses on your remote environments during your local builds through its own [recipe and plugin](https://docs.lando.dev/platformsh/). 

1. [Install Lando](https://docs.lando.dev/getting-started/installation.html).
1. Make sure Docker is already running - Lando will attempt to start Docker for you, but it's best to have it running in the background before beginning.
1. Start your apps and services with the command `lando start`.
1. To get up-to-date data from your Platform.sh environment ([services *and* mounts](https://docs.lando.dev/platformsh/sync.html#pulling)), run the command `lando pull`.
1. If at any time you have updated your Platform.sh configuration files, run the command `lando rebuild`.
1. When you have finished with your work, run `lando stop` and `lando poweroff`.

</details>
