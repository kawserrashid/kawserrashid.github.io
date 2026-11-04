// Loads about.json + quotes.json (About page copy) and validates them at build time.
import { z } from 'astro/zod';
import aboutRaw from '../data/about.json';
import quotesRaw from '../data/quotes.json';

const text = z.string().min(1);
const paragraphs = z.array(text).min(1);

const aboutSchema = z.object({
  meta: z.object({ title: text, description: text }),
  intro: z.object({ label: text, headline: text, paragraphs, portraitAlt: text }),
  interests: z.object({
    title: text,
    items: z
      .array(z.object({ title: text, icon: z.enum(['camera', 'question', 'headset']), text }))
      .min(1),
  }),
  path: z.object({
    title: text,
    items: z.array(z.object({ years: text, title: text, text })).min(1),
  }),
  lookingFor: z.object({
    title: text,
    paragraphs, // **double asterisks** mark bold text
    contactButton: text,
    cvButton: text,
    outsideWork: z.object({ label: text, text }),
  }),
  quotes: z.object({ label: text, title: text }),
});

const wordCount = (s: string) => s.trim().split(/\s+/).length;
const quotesSchema = z
  .array(
    z.object({
      text: text.refine((s) => wordCount(s) <= 30, 'Quotes must be 30 words or fewer'),
      author: text,
      source: text.optional(),
    }),
  )
  .min(1);

export const about = aboutSchema.parse(aboutRaw);
export const quotes = quotesSchema.parse(quotesRaw);
