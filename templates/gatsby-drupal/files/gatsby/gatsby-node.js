/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/node-apis/
 */

// You can delete this file if you're not using it

// Create a page for each article
const path = require('path');

exports.createPages = async ({ actions, graphql }) => {
  const { createPage } = actions;

  const articles = await graphql(`
    {
      allNodeArticle {
        nodes {
          title
          id
          body {
            processed
            summary
          }
          created
          path {
            alias
          }
          field_image {
            alt
          }
          relationships {
            field_image {
              localFile {
                publicURL
              }
            }
          }
        }
      }
    }
  `);

  articles.data.allNodeArticle.nodes.map(articleData =>
    createPage({
      path: articleData.path.alias,
      component: path.resolve(`src/templates/article.js`),
      context: {
        ArticleId: articleData.id,
      }
    })
  );
}
