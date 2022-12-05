# troubleshooting

- PHP 8.0 locally

    ```bash
    brew install php@8.0
    brew unlink php && brew link --overwrite --force php@8.0

    # Then remembering to reset
    brew unlink php && brew link php
    ```

- `composer create-project akeneo/pim-community-standard akeneo "6.0.*@stable" --ignore-platform-req=ext-apcu --ignore-platform-req=ext-imagick` with PHP 8.0
