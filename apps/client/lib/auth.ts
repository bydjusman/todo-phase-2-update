import { betterAuth } from 'better-auth';
import { betterAuthNextjsServerHandler } from 'better-auth/next-js/server-handler';

export const auth = betterAuth({
  secret: process.env.BETTER_AUTH_SECRET || 'super-secret-jwt-key-for-local-development-min-32-chars',
  emailAndPassword: {
    enabled: true,
  },
  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
  },
  database: {
    provider: 'sqlite',
    url: process.env.DATABASE_URL || 'sqlite://./todo_app.db',
  },
});

export const handler = betterAuthNextjsServerHandler(auth);
