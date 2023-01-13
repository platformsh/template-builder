import React from "react";
import PropTypes from "prop-types";
import { Link } from "gatsby";
import { GatsbyImage } from "gatsby-plugin-image"

const ArticlePreview = ({ title, path, image, alt, summary}) => (
  <div>
    <Link to={path}>
      <h2>{title}</h2>
    </Link>
    <GatsbyImage image={image} alt={alt} alignContent="center"/>
    <br /><br />
    <div dangerouslySetInnerHTML={{ __html: summary }} />
    <br /><br />
  </div>
);

ArticlePreview.propTypes = {
  title: PropTypes.string.isRequired,
  path: PropTypes.string.isRequired,
  image: PropTypes.string.isRequired,
  alt: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
}

export default ArticlePreview;
