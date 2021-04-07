import { useQuery, useMutation, gql, useSubscription } from "@apollo/client";

import Card from "./components/Card";

import "./App.scss";

const DEPLOY_FRIDAY_EPISODES_QUERY = gql`
  query {
    deployFridayEpisodes {
      id
      videoId
      title
      publishedAt
      description
      thumbnail {
        url
      }
      additionalInfo {
        upVotes
        downVotes
      }
    }
  }
`;

const UP_VOTE_MUTATION = gql`
  mutation upVote($id: String!) {
    upVote(id: $id)
  }
`;

const DOWN_VOTE_MUTATION = gql`
  mutation downVote($id: String!) {
    downVote(id: $id)
  }
`;

const UPDATED_VOTES_SUBSCRIPTION = gql`
  subscription votesUpdated {
    votesUpdated {
      _id
      upVotes
      downVotes
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(DEPLOY_FRIDAY_EPISODES_QUERY);
  const { data: { votesUpdated } = {} } = useSubscription(
    UPDATED_VOTES_SUBSCRIPTION
  );

  const [upVote] = useMutation(UP_VOTE_MUTATION);
  const [downVote] = useMutation(DOWN_VOTE_MUTATION);

  if (loading) {
    return "Loading...";
  }

  if (error) {
    return "Error...";
  }

  return (
    <div className="columns is-multiline is-justify-content-space-evenly">
      {data.deployFridayEpisodes.map((episode) => (
        <Card
          key={episode.videoId}
          episode={
            votesUpdated && votesUpdated._id === episode.id
              ? { ...episode, additionalInfo: votesUpdated }
              : episode
          }
          upVote={upVote}
          downVote={downVote}
        />
      ))}
    </div>
  );
}

export default App;
