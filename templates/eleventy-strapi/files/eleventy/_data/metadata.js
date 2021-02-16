const fs = require('fs');
const config = require("platformsh-config").config();
const localMeta = require("./metadata.json");

// String santizer; removes trailing slash from local API_URL environment variable.
function cleanUrl(url) {     
    return url.replace(/\/$/, "");
} 

// Update site-wide metadata when on a Platform.sh enviroment.
async function updateMetadata(){

    let metaDataNew = localMeta;

    // A few Platform.sh overrides. Feel free to remove or update.
    metaDataNew["author"]["name"] = "Platform.sh";
    metaDataNew["author"]["email"] = "sayhello@platform.sh";

    // The following detects whether on a Platform.sh environment, then updates URL metadata based on the
    //      PUBLIC_URL environment variable set in the committed .environment file.
    if ( config.isValidPlatform() ) {
        metaDataNew["url"] = cleanUrl(process.env.PUBLIC_URL);
        metaDataNew["feed"]["id"] = cleanUrl(process.env.PUBLIC_URL);
        metaDataNew["jsonfeed"]["url"] = cleanUrl(process.env.PUBLIC_URL) + metaDataNew["jsonfeed"]["path"];
        metaDataNew["author"]["url"] = cleanUrl(process.env.PUBLIC_URL) + "/about/";
    }

    return metaDataNew
}

module.exports = updateMetadata;
