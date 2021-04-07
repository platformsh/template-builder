const Card = ({ episode, upVote, downVote }) => {
  const {
    id,
    videoId,
    title,
    thumbnail: { url: thumbnailUrl },
    description,
    publishedAt,
    additionalInfo,
  } = episode;

  return (
    <div className="card column is-one-quarter-desktop is-one-third-tablet mx-4 my-4 is-flex is-flex-direction-column is-align-items-space-between">
      <header className="card-image">
        <figure className="image is-4by3">
          <img src={thumbnailUrl} alt={title} />
        </figure>
      </header>

      <main className="card-content is-flex-grow-1">
        <div className="media">
          <div className="media-content">
            <p className="title is-4">
              <a
                href={`https://youtube.com/watch?v=${videoId}`}
                target="_blank"
                rel="noreferrer"
              >
                {title}
              </a>
            </p>
          </div>
        </div>

        <div
          className="content has-text-justified"
          style={{
            wordBreak: "break-word",
          }}
        >
          {description.slice(0, 300) + "..."}
          <br />
          <br />
          <time dateTime={publishedAt}>
            {new Date(publishedAt).toLocaleDateString()}
          </time>
        </div>
      </main>

      <footer className="card-footer p-2 pt-4">
        <button
          className="card-footer-item button is-success"
          onClick={(_) => upVote({ variables: { id } })}
        >
          👍 {additionalInfo?.upVotes ?? 0}
        </button>
        <div className="is-flex-grow-1"></div>
        <button
          className="card-footer-item button is-danger"
          onClick={(_) => downVote({ variables: { id } })}
        >
          👎 {additionalInfo?.downVotes ?? 0}
        </button>
      </footer>
    </div>
  );
};

export default Card;
