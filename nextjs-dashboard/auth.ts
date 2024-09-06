// import NextAuth from 'next-auth';
// import Credentials from 'next-auth/providers/credentials';
// import { z } from 'zod';
// import { sql } from '@vercel/postgres';
// import type { User } from '@/app/lib/definitions';
// import bcrypt from 'bcrypt';
// import { authConfig } from './auth.config';

// async function getUser(email: string): Promise<User | undefined> {
//   try {
//     const result = await sql<User>`SELECT * FROM users WHERE email=${email}`;
//     return result.rows[0];
//   } catch (error) {
//     console.error('Failed to fetch user:', error);
//     throw new Error('Failed to fetch user.');
//   }
// }

// export const authOptions = {
//   ...authConfig,
//   providers: [
//     Credentials({
//       async authorize(credentials) {
//         const parsedCredentials = z
//           .object({ email: z.string().email(), password: z.string().min(6) })
//           .safeParse(credentials);

//         if (!parsedCredentials.success) {
//           console.log('Invalid credentials format');
//           return null;
//         }

//         const { email, password } = parsedCredentials.data;
//         const user = await getUser(email);

//         if (!user) {
//           console.log('User not found');
//           return null;
//         }

//         const passwordsMatch = await bcrypt.compare(password, user.password);
//         if (passwordsMatch) {
//           return user;
//         } else {
//           console.log('Invalid password');
//           return null;
//         }
//       }
//     })
//   ],
//   pages: {
//     signIn: '/auth/signin', // Customize sign-in page if needed
//     error: '/auth/error', // Error page
//   }
// };

// export default NextAuth(authOptions);
