const fetch = require("node-fetch");
const md = require("markdown-it")();
const config = require("platformsh-config").config();


// String santizer; removes trailing slash from local API_URL environment variable.
function cleanUrl(url) {     
  return url.replace(/\/$/, "");
} 

// function to get blogposts
async function getAllBlogposts() {
  // max number of records to fetch per query
  const recordsPerQuery = 100;

  // number of records to skip (start at 0)
  let recordsToSkip = 0;

  let makeNewQuery = true;

  let blogposts = [];

  var backend_route = "";
  // On Platform.sh, use the internal Strapi relationship.
  if ( config.isValidPlatform() ) {
    require("dotenv").config({
      path: `.env.${process.env.NODE_ENV}`,
    })
    backend_route = `http://${config.credentials("strapi")["host"]}/graphql`
  } else {
    // If a remote Strapi source is defined in a .env file, use that.
    require("dotenv").config()
    if (process.env.API_URL) {
      backend_route = `${cleanUrl(process.env.API_URL)}/graphql`;
    } else {
      // Otherwise, assume that the local Strapi server is running.
      backend_route = "http://localhost:1337/graphql";
    }
  }

  // make queries until makeNewQuery is set to false
  while (makeNewQuery) {
    try {
      // initiate fetch
      const data = await fetch(backend_route, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          query: `{
              articles {
              id
              title
              content
              author
              slug
              published_at
              created_at
              updated_at
            }
          }`,
        }),
      });

      // store the JSON response when promise resolves
      const response = await data.json();
      // handle CMS errors
      if (response.errors) {
        let errors = response.errors;
        errors.map((error) => {
          console.log(error.message);
        });
        throw new Error("Houston... We have a CMS problem");
      }

      // update blogpost array with the data from the JSON response
      blogposts = blogposts.concat(response.data.articles);

      // prepare for next query
      recordsToSkip += recordsPerQuery;

      // stop querying if we are getting back less than the records we fetch per query
      if (response.data.articles.length < recordsPerQuery) {
        makeNewQuery = false;
      }
    } catch (error) {
      throw new Error(error);
    }
  }

  // format blogposts objects
  const blogpostsFormatted = blogposts.map((item) => {
    return {
      id: item.id,
      title: item.title,
      slug: item.slug,
      body: md.render(item.content),
      author: item.author,
      published_at: item.published_at,
      published_data: item.published_date,
      created_at: item.created_at,
      updated_at: item.updated_at
    };
  });

  // return formatted blogposts
  return blogpostsFormatted;
}

// export for 11ty
module.exports = getAllBlogposts;
