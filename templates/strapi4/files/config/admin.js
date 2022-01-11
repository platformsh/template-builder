module.exports = ({ env }) => ({
  auth: {
    secret: env("ADMIN_JWT_SECRET", "b466455d-1488-461b-9d58-1940910d8373"),
  },
});
