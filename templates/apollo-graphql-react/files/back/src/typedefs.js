import { gql } from "apollo-server";

export default gql`
  type Episode {
    id: String!
    videoId: String!
    publishedAt: String!
    title: String!
    description: String
    thumbnail: Thumbnail!
    position: Int!
    additionalInfo: AdditionalInfo
  }

  type Thumbnail {
    url: String!
    width: Int!
    height: Int!
  }

  type AdditionalInfo {
    _id: String,
    upVotes: Int
    downVotes: Int
  }

  type Query {
    deployFridayEpisodes: [Episode]! @cacheControl(maxAge: 7200)
  }

  type Mutation {
    upVote(id: String!): Boolean
    downVote(id: String!): Boolean
  }

  type Subscription {
    votesUpdated: AdditionalInfo
  }
`;
