if [ -f install/platform.installed ]; then
    # If the site is already installed, it's safe to run these
    # once the site is open again post-deploy.
    # If that's not the case for your site, move these two lines
    # to the else block at the end of deploy.sh.
    rsync -avq --update --ignore-errors _public/ public/
    bundle exec rake assets:precompile -q
fi
