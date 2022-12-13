import React from "react";
import PropTypes from "prop-types";
import { graphql } from "gatsby";
import { Link } from "gatsby"
import { GatsbyImage, getImage} from "gatsby-plugin-image"
import Layout from "../components/layout"

const Article = ({ data }) => {
  const post = data.nodeArticle;
  const image = getImage(post.relationships.field_image.localFile.childImageSharp.gatsbyImageData)

  return (
    <Layout>
      <h1>{ post.title }</h1>
      <Link to="/articles/">
        <h4>Back to All Articles</h4>
      </Link>
      <GatsbyImage image={image}  alt={ post.field_image.alt } />
      <br/><br/>
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
      id
      title
      body {
        processed
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
              gatsbyImageData
            }
          }
        }
      }
    }
  }
`;

export default Article;
