import React from "react";
import PropTypes from "prop-types";
import { Link } from "gatsby";
import Img from "gatsby-image";

const ArticlePreview = ({ title, path, image, alt, summary }) => (
  <div>
    <Link to={path}>
      <h2>{title}</h2>
    </Link>
    <Img fluid={image} alt={alt} />
    <div dangerouslySetInnerHTML={{ __html: summary }} />
    <br /><br />
  </div>
);

ArticlePreview.propTypes = {
  title: PropTypes.string.isRequired,
  path: PropTypes.string.isRequired,
  image: PropTypes.string.isRequired,
  alt: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired
}

export default ArticlePreview;
