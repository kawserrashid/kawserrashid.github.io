// Collection schemas: the site's "database tables" (docs/03-content-schema.md).
// `astro build` validates every Markdown/JSON record against these, like a
// migration check: a missing field or wrong value fails the build (FR-10).
import { defineCollection } from 'astro:content';
import { glob, file } from 'astro/loaders';
import { z } from 'astro/zod';
import { orPlaceholder, statusEnum } from './lib/schema';

const research = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/research' }),
  schema: ({ image }) =>
    z
      .object({
        title: z.string(),
        summary: z.string().max(160),
        topic: z.string(), // free text (PM decision 2026-11-04)
        status: statusEnum,
        date: z.coerce.date(), // "planted"
        // Optional until real images exist; the card shows a placeholder slot.
        cover: image().optional(),
        coverAlt: z.string().min(1).optional(),
        code: z.url().optional(),
        demo: z.url().optional(),
        draft: z.boolean().default(false),
      })
      .refine((d) => !d.cover || d.coverAlt, {
        message: 'coverAlt is required when cover is set',
        path: ['coverAlt'],
      }),
});

const notes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/notes' }),
  schema: z.object({
    title: z.string(),
    status: statusEnum,
    date: z.coerce.date(),
    draft: z.boolean().default(false),
  }),
});

const paperNotes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/paper-notes' }),
  schema: z.object({
    paperTitle: z.string(),
    venue: z.string(),
    year: orPlaceholder(z.number().int().min(1900)),
    written: z.coerce.date(),
  }),
});

const publications = defineCollection({
  loader: file('src/data/publications.json'),
  schema: z
    .object({
      type: z.enum(['conference', 'manuscript', 'thesis']),
      title: z.string(),
      authors: z.array(z.string()).min(1),
      venue: z.string(),
      year: orPlaceholder(z.number().int().min(1900)),
      status: orPlaceholder(z.enum(['under-review', 'in-preparation'])).optional(),
      pdf: z.url().optional(),
      doi: z.string().regex(/^10\.\d{4,}\/\S+$/, 'DOI must look like 10.xxxx/…').optional(),
    })
    .refine((p) => (p.type === 'manuscript') === (p.status !== undefined), {
      message: 'status is required for manuscripts and only allowed on manuscripts',
      path: ['status'],
    }),
});

export const collections = { research, notes, paperNotes, publications };
