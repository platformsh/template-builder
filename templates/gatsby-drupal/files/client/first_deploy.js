const http = require("http");

function decode(value) {
    return JSON.parse(Buffer.from(value, 'base64'));
}

const projectID = `${process.env.PLATFORM_PROJECT}`;
const environment = `${process.env.PLATFORM_BRANCH}`;
const redeployLink = `https://console.platform.sh/projects/${projectID}/${environment}/actions/redeploy`;

let backendURL;
let routes = decode(process.env.PLATFORM_ROUTES);
for (route in routes) {
    if (routes[route]['id'] == 'api') {
       backendURL = route;
    }
}

const backendLogin = `${backendURL}user/login`;
const credentialUpdate = `${backendURL}user/1/edit`

const outputString = `

<!DOCTYPE html>
<html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Overpass:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
        <style>
            html, body {
                height: 100%;
                font-family: 'Overpass', sans-serif;
            }
            .container * {
                position: relative;
            }
            a { 
                color: #145CC6;
                text-decoration: none;
            }
            a:visited {
                color: #145CC6; 
            }
            a:hover {
                text-decoration: underline;
            }
            .container {  display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: 15% 75% 10%;
            gap: 0px 0px;
            grid-auto-flow: row;
            grid-template-areas:
                "header"
                "main"
                "footer";
            }

            .header {  display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: 20% 1fr;
            gap: 0px 0px;
            grid-auto-flow: row;
            grid-template-areas:
                "callouts"
                "logo-area";
            grid-area: header;
            }

            .callouts {  display: grid;
            grid-template-columns: 40% 1fr;
            grid-template-rows: 1fr;
            gap: 0px 0px;
            grid-auto-flow: row;
            grid-template-areas:
                "callouts-left callouts-right";
            grid-area: callouts;
            }

            .callouts-left { grid-area: callouts-left; }

            .callouts-right { 
                grid-area: callouts-right;
                background-color: #ffbdbb;
            }

            .logo-area {  display: grid;
            grid-template-columns: 40% 1fr;
            grid-template-rows: 1fr;
            gap: 0px 0px;
            grid-auto-flow: row;
            grid-template-areas:
                "logo-area-left logo-area-right";
            grid-area: logo-area;
            }

            .logo-area-left { 
                grid-area: logo-area-left; 
                padding-left: 80px;
            }

            .logo-area-right { 
                grid-area: logo-area-right; 
                background-color: #ffbdbb;
            }

            .logo {
                margin: 0;
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
            }

            .main {  display: grid;
            grid-template-columns: 40% 1fr;
            grid-template-rows: 1fr;
            gap: 0px 0px;
            grid-auto-flow: row;
            grid-template-areas:
                "template-details template-nextsteps";
            grid-area: main;
            }

            .template-details { 
                grid-area: template-details; 
                padding: 80px 80px 80px 80px;
            }

            .template-details-block {
                /* background-color: yellow; */
                /* border: 1px solid gray; */
                width: 100%;
                height: 100%;
                display: grid;
                grid-template-columns: 1fr;
                grid-template-rows: 1fr 1fr;
                gap: 0px 0px;
                grid-auto-flow: row;
                grid-template-areas:
                    "template-logo"
                    "template-logo-details";
            }

            .template-logo { 
                grid-area: template-logo; 
                margin: 40px 40px 20px 40px;
            }

            .template-logo > .api {
                margin: 0;
                position: absolute;
                top: 50%;
                left: 10%;
                transform: translateY(-50%);
                width: 35%;
            }

            .template-logo > .client {
                margin: 0;
                position: absolute;
                top: 50%;
                right: 10%;
                transform: translateY(-50%);
                width: 35%;
            }

            .template-logo-details { 
                grid-area: template-logo-details; 
                margin: 20px 40px 40px 40px;
                color: #444344;
                align-items: center;
            }

            .template-nextsteps { 
                grid-area: template-nextsteps; 
                background-color: #ffbdbb;
                padding: 80px 80px 120px 80px;

            }

            .template-instructions-block {
                background-color: white;
                box-shadow: 0 6px 24px rgb(73 71 95 / 35%);
                width: 100%;
                height: 100%;
                display: grid;
                grid-template-columns: 1fr;
                grid-template-rows: .25fr .75fr;
                gap: 0px 0px;
                grid-auto-flow: row;
                grid-template-areas:
                    "details-header"
                    "details-content";

            }

            .details-header {  display: grid;
            grid-template-columns: .45fr 1fr;
            grid-template-rows: 1fr;
            gap: 0px 0px;
            grid-auto-flow: row;
            grid-template-areas:
                "header-col header-colb";
            grid-area: details-header;
            }

            .header-cola { 
                grid-area: header-col; 
                // background-color: #f4f2f3;
                padding: 20px;
                border-bottom: 1px solid #eae5e7;
                padding-bottom: 16px;
                font-weight: 700;
                font-size: 14px;
                line-height: 1.5;
                letter-spacing: .1em;
                text-transform: uppercase;
                color: #797477;
            }

            .header-colb { 
                grid-area: header-colb; 
                padding: 20px;
                border-bottom: 1px solid #eae5e7;
                padding-bottom: 16px;
                font-weight: 700;
                font-size: 14px;
                line-height: 1.5;
                letter-spacing: .1em;
                text-transform: uppercase;
                color: #797477;            }


            .details-content {  
                display: grid;
                grid-template-columns: .45fr 1fr;
                grid-template-rows: 1fr;
                gap: 0px 0px;
                grid-auto-flow: row;
                grid-template-areas:
                    "content-cola content-colb";
                grid-area: details-content;
            }

            .content-cola { 
                grid-area: content-cola; 
                // background-color: #f4f2f3;
                padding: 20px;
            }

            .content-colb { 
                
                grid-area: content-colb; 
                padding: 20px;
            
            }

            pre {
                // text-align: center;
                background: #eae5e7;
                padding: 10px 10px 10px 10px;
                white-space: pre-wrap;       /* css-3 */
                white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
                white-space: -pre-wrap;      /* Opera 4-6 */
                white-space: -o-pre-wrap;    /* Opera 7 */
                word-wrap: break-word;       /* Internet Explorer 5.5+ */
            }

            code {
                font-size: 1.1em;
                background: #eae5e7;
                // padding: 2px 10px 2px 10px;
                border-radiux: 2px;
            }

            .footer {  
                display: grid;
                grid-template-columns: 40% 1fr;
                grid-template-rows: 1fr;
                gap: 0px 0px;
                grid-auto-flow: row;
                grid-template-areas:
                    "footer-left footer-right";
                grid-area: footer;
            }

            .footer-left { grid-area: footer-left; }

            .footer-right { 
                grid-area: footer-right; 
                background-color: #ffbdbb;
            }


            html, body , .container {
                height: 100%;
                margin: 0;
            }



        </style>
    </head>
<body>

    <div class="container">
        <div class="header">
          <div class="callouts">
            <div class="callouts-left"></div>
            <div class="callouts-right"></div>
          </div>
          <div class="logo-area">
            <div class="logo-area-left">
                <div class="logo">
                    <a href="https://platform.sh">
                        <img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="200px">
                    </a>
                </div>
            </div>
            <div class="logo-area-right"></div>
          </div>
        </div>
        <div class="main">
          <div class="template-details">
              <div class="template-details-block">
                <div class="template-logo">
                    <img class="api" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xNi4yIDMuOUMxNi4yIDMuOSAxNC44MiAzLjMgMTQuMDQgMi44MkMxNC4wNCAyLjgyIDEzLjAyIDIuMjIgMTEuMzQgMEMxMS4zNCAwIDExLjQgMi41MiA4LjcgMy44NEM0LjQ0IDUuNTIgMS44IDkuMDYgMS44IDEzLjU2QzEuOCAxOS4yNiA2LjQ4IDIzLjk0IDEyLjE4IDIzLjk0QzE3Ljk0IDIzLjk0IDIyLjU2IDE5LjI2IDIyLjU2IDEzLjU2QzIyLjYyIDYuNiAxNi4yIDMuOSAxNi4yIDMuOVpNNC42OCA5LjZDMy4wNiA5Ljk2IDMuMTggOS4xMiAzLjQ4IDguNEMzLjYgNy45OCA0LjAyIDcuNSA0LjAyIDcuNUM1LjEgNS43NiA3LjUgNC41IDcuNSA0LjVDNy44IDQuMzggOC4zNCA0LjA4IDguODIgMy44NEM5Ljc4IDMuMyAxMC4wMiAzIDEwLjAyIDNDMTEuNCAxLjY4IDExLjI4IDAuMDYgMTEuMjggMEMxMi40OCAyLjQgMTEuMDQgMy40OCAxMS4wNCAzLjQ4QzExLjQgMy44NCAxMS4yOCA0LjIgMTEuMjggNC4yQzkuNDIgOC4yMiA0LjY4IDkuNiA0LjY4IDkuNlpNMTcuMjIgMjIuMkMxNy4xIDIyLjI2IDE1LjYgMjIuOTggMTMuODYgMjIuOThDMTIuOSAyMi45OCAxMS44OCAyMi43NCAxMC45OCAyMi4xNEMxMC42OCAyMS45IDEwLjU2IDIxLjQ4IDEwLjc0IDIxLjE4QzEwLjggMjEuMDYgMTEuMTYgMjAuNjQgMTIgMjEuMThDMTIuMDYgMjEuMjQgMTQuMDQgMjIuNTYgMTcuMSAyMC44OEMxNy4zNCAyMC43NiAxNy42NCAyMC44MiAxNy43NiAyMS4wNkMxNy45NCAyMS4zIDE4IDIxLjc4IDE3LjIyIDIyLjJaTTEzLjAyIDE5LjY4TDEzLjA4IDE5LjYyQzEzLjE0IDE5LjU2IDE0LjE2IDE4LjI0IDE1LjY2IDE4LjQyQzE1LjkgMTguNDIgMTYuNzQgMTguNDggMTcuMjggMTkuNUMxNy4zNCAxOS42MiAxNy40NiAyMC4wNCAxNy4yMiAyMC4zNEMxNy4xIDIwLjQ2IDE2LjkyIDIwLjU4IDE2LjU2IDIwLjQ2QzE2LjMyIDIwLjQgMTYuMiAyMC4xNiAxNi4yIDIwLjA0QzE2LjE0IDE5Ljg2IDE2LjA4IDE5Ljc0IDE1LjQ4IDE5LjY4QzE1IDE5LjYyIDE0LjcgMTkuODYgMTQuMzQgMjAuMTZDMTQuMTYgMjAuMzQgMTMuOTIgMjAuNTIgMTMuNjggMjAuNThDMTMuNjIgMjAuNjQgMTMuNTYgMjAuNjQgMTMuNDQgMjAuNjRDMTMuMzIgMjAuNjQgMTMuMiAyMC41OCAxMy4wOCAyMC41MkMxMi45IDIwLjM0IDEyLjg0IDIwLjEgMTMuMDIgMTkuNjhaTTE5Ljg2IDE5LjhDMTkuODYgMTkuOCAxOS4zMiAxOS45OCAxOC43OCAxOS4zOEMxOC43OCAxOS4zOCAxNy4xNiAxNy41MiAxNi4zOCAxNy4yMkMxNi4zOCAxNy4yMiAxNS45IDE3LjA0IDE1LjMgMTcuMjhDMTUuMyAxNy4yOCAxNC44OCAxNy4zNCAxMy4yNiAxOC40MkMxMy4yNiAxOC40MiAxMC41IDIwLjE2IDkuMTIgMTkuOTJDOS4xMiAxOS45MiA2IDE5Ljk4IDYuNDIgMTYuNjhDNi40MiAxNi42OCA3LjA4IDEyLjk2IDExLjQgMTMuOEMxMS40IDEzLjggMTIuMzYgMTMuOTggMTQuMSAxNS4zNkMxNC4xIDE1LjM2IDE1LjMgMTYuMjYgMTUuOSAxNi4yNkMxNS45IDE2LjI2IDE2LjM4IDE2LjMyIDE3LjQ2IDE1LjY2QzE3LjQ2IDE1LjY2IDE5LjU2IDE0LjA0IDIwLjM0IDE0LjFDMjAuNDYgMTQuMSAyMS44NCAxNC4wNCAyMS44NCAxNi4zMkMyMS43OCAxNi4yNiAyMS44NCAxOC45IDE5Ljg2IDE5LjhaIiBmaWxsPSIjMDA4RUNFIi8+Cjwvc3ZnPgo=" width="100%">
                    <img class="client" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='225' height='225'%3E%3Cg %3E%3Cpath d='M112.5 0A112.5 112.5 0 1 0 225 112.5 112.5 112.5 0 0 0 112.5 0zM24.17 113.67l87.16 87.16a88.35 88.35 0 0 1-87.16-87.16zm108.1 85L26.38 92.73a88.35 88.35 0 0 1 157.54-32.22L171.69 71.3a72.13 72.13 0 0 0-127 16.64l92.38 92.38a72.26 72.26 0 0 0 45.46-50.51h-38.3V112.5h56.61a88.38 88.38 0 0 1-68.57 86.12z' style='fill:%23744c9e' /%3E%3C/g%3E%3C/svg%3E">

                                </div>
                <div class="template-logo-details">
                    <p>Congrats! You've just deployed the Gatsby Drupal demo template for Platform.sh!</p>
                    <p>This template has already configured the multi-app relationship for you, which will work automatically across every development environment you create from this point forward. Be sure to follow the instructions on the right to complete the demo.</p>
                </div>
              </div>
          </div>
          <div class="template-nextsteps">
            <div class="template-instructions-block">
                <div class="details-header">
                    <div class="header-cola">About</div>
                    <div class="header-colb">Next steps</div>
                  </div>
                  <div class="details-content">
                    <div class="content-cola">
                        <p>When you deployed this template, a few things happend.</p>
                        <p>Drupal was fully installed, all of the necessary modules and settings were configured to communicate with the Gatsby frontend, and connection credentials were shared with that frontend application.</p>
                        <p>Now that that's completed, there are only two steps you'll need to take to complete the demo.</p>
                        <p>If anything seems unclear, be sure to check out the <a href="https://github.com/platformsh-templates/nextjs-drupal" target="_blank" rel="noopener noreferrer">README</a> for more details.
                    
                        </div>
                    <div class="content-colb">
                        <p><strong>1. Update your Drupal admin credentials</strong></p>
                        <p>Drupal has been installed, and an admin user was created. <a href="${backendLogin}" target="_blank" rel="noopener noreferrer">Visit the Drupal login page</a>, then <a href="${credentialUpdate}" target="_blank" rel="noopener noreferrer">update your email and password</a> to something more memorable.</p>
                        <ul>
                            <li>username: <code>admin</code></li>
                            <li>password: <code>${process.env.PLATFORM_PROJECT_ENTROPY}</code></li>
                        </ul>
                        <p><strong>2. Rebuild the environment</strong></p>
                        <p>Platform.sh is secure by default. Part of that security involves read-only access to the file system and container isolation during the build process. Because of this, credentials for the frontend application were not yet available for the first Gatsby build.</p>
                        <p>No worries! This will only be the case on this first deployment. To view the final frontend build, all we need to do is rebuild the Platform.sh environment and restart the container.</p>
                        <p>To do this, we just need to add a variable using the <a href="https://docs.platform.sh/development/cli.html" target="_blank" rel="noopener noreferrer">Platform.sh CLI</a>:</p>
                        <pre><code>platform variable:create -p ${projectID} -e ${environment} -l environment --name DEPLOY --value FRIDAY --visible-build=true --prefix=env: -n</code></pre>
                     </div>
                  </div>
            </div>
          </div>
        </div>
        <div class="footer">
          <div class="footer-left"></div>
          <div class="footer-right"></div>
        </div>
      </div>

</body>
</html> 
`;

const server = http.createServer(async function(_request, response) {
  
    response.writeHead(200, { "Content-Type": "text/html" });
    response.end(outputString);
  });
  
  // Get PORT and start the server
  server.listen(process.env.PORT, function() {
    console.log(`Listening on port ${process.env.PORT}`);
});
