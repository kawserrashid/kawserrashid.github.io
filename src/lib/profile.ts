// Loads profile.json and validates it at build time (FR-09, FR-10).
// Like a Pydantic model: bad data fails `astro build` with a clear message.
import { z } from 'astro/zod';
import { orPlaceholder } from './schema';
import raw from '../data/profile.json';

const profileSchema = z.object({
  name: z.string().min(1),
  tagline: z.string().min(1),
  email: orPlaceholder(z.email()),
  location: z.string().min(1),
  links: z.object({
    github: orPlaceholder(z.url()),
    scholar: orPlaceholder(z.url()),
    linkedin: orPlaceholder(z.url()),
  }),
  now: z.object({
    text: z.array(z.string().min(1)).min(1), // one string per paragraph
    updated: z.string().regex(/^\d{4}-(0[1-9]|1[0-2])$/, 'now.updated must be YYYY-MM'),
  }),
});

export const profile = profileSchema.parse(raw);
