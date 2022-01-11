# Regarding `.env`

Symfony's composer install script creates a `.env` file, but (incorrectly) doesn't include it in the `.gitignore`.  It does create a `.gitignore` if one does not already exist.  If it does exist, it ignores it.

That creates an interesting problem if we want to add `.env` to the `.gitignore` file by patch, since the first time through the patch will apply, but subsequent runs will fail because the file is already patched.

Absent a good solution, the patch file is named in such a way as to not get used, but is retained for documentation purposes.  If the template needs to be rebuilt from scratch for some reason, the patch will need to be temporarily re-activated.
