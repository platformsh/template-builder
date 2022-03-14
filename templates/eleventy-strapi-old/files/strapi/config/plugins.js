// Strapi does not come with e-mail support out of the box. This plugin configures e-mail on 
//  Platform.sh using the `strapi-provider-email-nodemailer` module. 
//  Note that on Platform.sh, e-mail is enabled only on Master by default.
module.exports = ({ env }) => ({
    email: {
      provider: 'nodemailer',
      providerOptions: {
        host: env('PLATFORM_SMTP_HOST', 'smtp.example.com'),
        port: env('PLATFORM_SMTP_PORT', 587),
      },
      settings: {
        defaultFrom: 'no-reply@strapi.io',
        defaultReplyTo: 'no-reply@strapi.io',
      }
    }
  });
