# Prestashop template for Flexible Web Publisher on Platform.sh

## How to install

1. Clone this repository
2. Create a new platform.sh project

```
platform project:create
```

3. Add specific environment variables

```
platform -p<project> variable:set ADMIN_EMAIL your@email.com
platform -p<project> variable:set ADMIN_PASSWORD yourpassword
```

4. Push to platform.sh

```
git remote add platform <project id>@git.<project region>.platform.sh:<project id>.git
git push platform master
```

5. Backend

You can access your backend at `/admin-fwp` with the credentials that you defined as variables.
