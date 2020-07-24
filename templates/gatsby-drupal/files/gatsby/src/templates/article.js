import React from "react";
import PropTypes from "prop-types";
import { graphql } from "gatsby";
import { Link } from "gatsby"

import Layout from "../components/layout"

const Article = ({ data }) => {
  const post = data.nodeArticle;

  return (
    <Layout>
      <h1>{ post.title }</h1>
      <Link to="/articles/">
        <h4>Back to All Articles</h4>
      </Link>
      <img
        src={ post.relationships.field_image.localFile.publicURL }
        alt={ post.field_image.alt }
      />
      <div dangerouslySetInnerHTML={{ __html: post.body.processed }}
      />
    </Layout>
  );
};

Article.propTypes = {
  data: PropTypes.object.isRequired,
}

export const query = graphql `
  query($ArticleId: String!) {
    nodeArticle(id: {eq: $ArticleId}) {
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
`;

export default Article;
