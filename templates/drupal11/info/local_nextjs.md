<details>
<summary><strong>Next.js: building the frontend locally</strong></summary><br />

After you have created a new environment, you can connect to a backend Drupal instance and develop the frontend locally with the following steps.

1. `cd client`
1. Update the environment variables for the current environment by running `./get_local_config.sh`. This will pull the generated `.env.local` file for the current environment.

   ```bash
   # This .env file is generated programmatically within the backend Drupal app for each Platform.sh environment
   # and stored within an network storage mount so it can be used locally.

   NEXT_PUBLIC_DRUPAL_BASE_URL=https://api.ENVIRONMENT-HASH-PROJECTID.REGION.platformsh.site
   NEXT_IMAGE_DOMAIN=api.ENVIRONMENT-HASH-PROJECTID.REGION.platformsh.site
   DRUPAL_SITE_ID=nextjs_site
   DRUPAL_FRONT_PAGE=/node
   DRUPAL_CLIENT_ID=CONSUMER_CLIENT_ID
   DRUPAL_CLIENT_SECRET=GENERATED_SECRET
   ```

1. Install dependencies: `yarn --frozen-lockfile`.
1. Run the development server: `yarn dev`. Next.js will then run on http://localhost:3000.

</details>
