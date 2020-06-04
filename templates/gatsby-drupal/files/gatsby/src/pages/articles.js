import React from "react";
import PropTypes from "prop-types";
import {graphql} from "gatsby";

import Layout from "../components/layout";
import ArticlePreview from "../components/articlePreview"


const Articles = ({ data }) => {
  const articles = data.allNodeArticle.nodes;

  return (
    <Layout>
      <h1>Articles</h1>
      {articles.map(article => (
        <ArticlePreview
          key={article.id}
          title={article.title}
          path={article.path.alias}
          image={article.relationships.field_image.localFile.childImageSharp.fluid}
          alt={article.field_image.alt}
          summary={article.body.summary ? article.body.summary : article.body.processed.substring(0, 300)}
        />
      ))}
    </Layout>
  );
}

Articles.propTypes = {
  data: PropTypes.object.isRequired,
}

export const data = graphql `
  {
    allNodeArticle(sort: {fields: created, order: DESC}) {
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
              childImageSharp {
                fluid(maxWidth: 600) {
                  ...GatsbyImageSharpFluid
                }
              }
            }
          }
        }
      }
    }
  }
`;


export default Articles;
