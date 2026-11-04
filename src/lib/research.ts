// Loads research.json (Research page copy) and validates it at build time.
import { z } from 'astro/zod';
import raw from '../data/research.json';

const text = z.string().min(1);

const researchPageSchema = z.object({
  title: text,
  intro: text,
  publications: z.object({ title: text }),
  writeups: z.object({ title: text, hint: text }),
});

export const researchPage = researchPageSchema.parse(raw);
